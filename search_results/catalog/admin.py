from django.contrib import admin
from .models import USPTO_Patent_Search_Result
from .models import USPTO_Documents
# Register your models here.

admin.site.register(USPTO_Patent_Search_Result)
admin.site.register(USPTO_Documents)