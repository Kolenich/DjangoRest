from django.contrib import admin
from api.models import Employee, Organization, Attachment

# Register your models here.
admin.site.register(Employee, Organization, Attachment)
