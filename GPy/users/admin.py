from django.contrib import admin
from .models import Author, Editor, Reader
from GPy.admin_site import custom_admin_site

@admin.register(Author, Reader, Editor, site=custom_admin_site)
class PersonAdmin(admin.ModelAdmin):
    pass
