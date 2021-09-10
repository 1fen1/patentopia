<<<<<<< HEAD
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import sqlite3
import requests

sqlite_file = 'search_results/db.sqlite3'
conn = sqlite3.connect(sqlite_file)

print('Введите первое ключевое слово')
keyword1 = input()
print('Введите второе ключевое слово')
keyword2 = input()
print('Введите союз AND, OR или ANDNOT')
union = input()

url = 'https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1='+keyword1+'&FIELD1=&co1='+union+'&TERM2='+keyword2+'&FIELD2=&d=PTXT'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")

strongs = page_soup.select('i > strong')
results_amount = int(strongs[2].getText())

for i in range(1, results_amount+1):
    link = 'https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r='+str(i)+'&f=G&l=50&co1='+union+'&d=PTXT&s1='+keyword1+'&s2='+keyword2+'&OS='+keyword1+'+'+union+'+iron&RS='+keyword1+'+'+union+'+'+keyword2
    req = Request(link , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")

    titles = page_soup.find('font', {'size':'+1'})
    title = " ".join(titles.getText().split())

    pat_nums = page_soup.find_all('b')
    pat_num = pat_nums[1].getText()

    doc_type = pat_nums[0].getText()+';'+pat_nums[2].getText()
    doc_type = " ".join(doc_type.split())

    date_of_pat = " ".join(pat_nums[3].getText().split())

    abstracts = page_soup.find("b", text="Abstract")
    if abstracts != None:
        abstract = " ".join(abstracts.next_element.next_element.next_element.getText().split())

    inventors = page_soup.find("th", text="Inventors:")
    if inventors != None:
        inventor = " ".join(inventors.next_element.next_element.next_element.getText().split())

    applicants = page_soup.find_all("td", align="left", width="90%")[1]
    if applicants != None:
        applicant = " ".join(applicants.text.split())

    assignees = page_soup.find("th", text="Assignee:")
    if assignees != None:
        assignee = " ".join(assignees.next_element.next_element.next_element.getText().split())

    # family_ids = assignees.next_sibling.next_element.next_element.next_element.next_element.next_element
    # family_id = " ".join(family_ids.getText().split())

    # appl_nos = family_ids.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    # appl_no = " ".join(appl_nos.getText().split())

    # date_of_appls = appl_nos.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    # date_of_appl = " ".join(date_of_appls.getText().split())

    prior_pub_datas = page_soup.find("u", text="Publication Date")
    if prior_pub_datas != None:
        prior_pub_data = " ".join(prior_pub_datas.next_element.next_element.getText().split())

    related_us_docs = page_soup.find("u", text="Issue Date")
    if related_us_docs != None:
        related_us_doc = " ".join(related_us_docs.next_element.next_element.next_element.getText().split())

    current_us_classs = page_soup.find("b", text="Current U.S. Class:")
    if current_us_classs != None:
        current_us_class = " ".join(current_us_classs.next_element.next_element.next_element.getText().split())

    current_cpc_classs = page_soup.find("b", text="Current CPC Class: ")
    if current_cpc_classs != None:
        current_cpc_class = " ".join(current_cpc_classs.next_element.next_element.next_element.getText().split())

    current_int_classs = page_soup.find("b", text="Current International Class: ")
    if current_int_classs != None:
        current_int_class = " ".join(current_int_classs.next_element.next_element.next_element.getText().split())

    field_of_searchs = page_soup.find("b", text="Field of Search: ")
    if field_of_searchs != None:
        field_of_search = " ".join(field_of_searchs.next_element.next_element.next_element.getText().split())

    us_patent_docs = page_soup.find("b", text="U.S. Patent Documents")
    us_patent_doc_link = []
    us_patent_doc_text = []
    if us_patent_docs != None:
        us_patent_doc = us_patent_docs.next_element.next_element.next_element
        for a in us_patent_doc.find_all('td'):
            us_patent_doc_text.append(" ".join(a.getText().split()))
        us_patent_doc_text = list(filter(None, us_patent_doc_text))
        for a in us_patent_doc.find_all(href=True):
            us_patent_doc_link.append(a['href'])

    foreign_patent_docs = page_soup.find("b", text="Foreign Patent Documents")
    foreign_patent_doc_text = []
    if foreign_patent_docs != None:
        foreign_patent_doc = foreign_patent_docs.next_element.next_element.next_element
        for a in foreign_patent_doc.find_all('td'):
            foreign_patent_doc_text.append(" ".join(a.getText().split()))
        foreign_patent_doc_text = list(filter(None, foreign_patent_doc_text))

    other_referencess = page_soup.find("b", text="Other References")
    if other_referencess != None:
        other_references = other_referencess.next_element.next_element.next_element.getText()

    #attorneys = page_soup.find("i", text="Attorney, Agent or Firm:")
    #if attorneys != None:
    #    attorney = " ".join(attorneys.next_element.next_element.next_element.next_element.next_element.split())

#     pdf_file = page_soup.select_one('a[href*=Docid]')
#     pdf_file = str(pdf_file)
#     pdf_file = pdf_file[44:52]
#     pdf_file_link = "https://pdfpiw.uspto.gov/"+pdf_file[6:8]+"/"+pdf_file[3:6]+"/"+pdf_file[0:3]+"/1.pdf"
#     r = requests.get(pdf_file_link, stream = True)
#     with open("USPTO/"+pat_num+".pdf", "wb") as pdf:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:
#                 pdf.write(chunk)

    cursor = conn.cursor()
    sqlite_insert_query = """INSERT INTO USPTO_Patent_Search_Result (search_imput, title, pat_no, link, date_added, date_updated) VALUES (?, ?, ?, ?, 'None', 'None');"""
    data_tuple = (keyword1+' '+union+' '+keyword2, title, pat_num, link)
    cursor.execute(sqlite_insert_query, data_tuple)
    conn.commit()
    sqlite_insert_query = """INSERT INTO USPTO_Documents (title, pat_num, doc_type, date_of_pat, abstract, applicant, assignee, family_id, appl_no, date_of_appl, prior_pub_data, related_us_doc, current_us_class, current_int_class, field_of_search, referenced_us_patent_doc_text, referenced_us_patent_doc_link, referenced_foreign_patent_doc, other_references, attorney_agent_firm) VALUES (?, ?, ?, ?, ?, ?, ?, 'None', 'None', 'None', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'None');"""
    data_tuple = (title, pat_num, doc_type, date_of_pat, abstract, applicant, assignee, prior_pub_data, related_us_doc, current_us_class, current_int_class, field_of_search, map(str, us_patent_doc_text), map(str, us_patent_doc_link), map(str, foreign_patent_doc_text), other_references)
    cursor.execute(sqlite_insert_query, data_tuple)
    conn.commit()
    cursor.close()