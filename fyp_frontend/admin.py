from django.contrib import admin
from .models import Captcha
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Captcha)
class userdata(ImportExportModelAdmin) :
    pass