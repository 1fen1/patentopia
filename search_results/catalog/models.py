from django.db import models

# Create your models here.

class USPTO_Patent_Search_Result(models.Model):
    search_imput = models.CharField(max_length=100, help_text="Введенныt ключевые слова")
    title = models.CharField(max_length=100, help_text="Результат поиска")
    pat_no = models.CharField(max_length=100, default='UNKNOWN', help_text="Номер патента")
    link = models.CharField(max_length=1000, default='UNKNOWN', help_text="Ссылка на патент")
    date_added = models.CharField(max_length=20, default='UNKNOWN', help_text="Дата добавления патента")
    date_updated = models.CharField(max_length=20, default='UNKNOWN', help_text="Дата изменения патента")

    def __str__(self):
        return self.pat_no

    class Meta:
        db_table = "USPTO_Patent_Search_Result"

class USPTO_Documents(models.Model):
    pat_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, default='None')
    pat_num = models.CharField(max_length=100, default='None')
    doc_type = models.CharField(max_length=100, default='None')
    date_of_pat = models.CharField(max_length=100, default='None')
    abstract = models.CharField(max_length=1000, default='None')
    applicant = models.CharField(max_length=1000, default='None')
    assignee = models.CharField(max_length=1000, default='None')
    family_id = models.CharField(max_length=100, default='None')
    appl_no = models.CharField(max_length=100, default='None')
    date_of_appl = models.CharField(max_length=100, default='None')
    prior_pub_data = models.CharField(max_length=1000, default='None')
    related_us_doc = models.CharField(max_length=10000, default='None')
    current_us_class = models.CharField(max_length=100, default='None')
    current_int_class = models.CharField(max_length=100, default='None')
    field_of_search = models.CharField(max_length=1000, default='None')
    referenced_us_patent_doc_text = models.CharField(max_length=10000, default='None')
    referenced_us_patent_doc_link = models.CharField(max_length=10000, default='None')
    referenced_foreign_patent_doc = models.CharField(max_length=10000, default='None')
    other_references = models.CharField(max_length=10000, default='None')
    attorney_agent_firm = models.CharField(max_length=100, default='None')

    def __str__(self):
        return self.pat_num
    
    class Meta:
        db_table = "USPTO_Documents"