from django.contrib import admin

# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header: str = 'Bookr Administration Rodrigo'


admin_site = BookrAdmin(name='bookr_admin')