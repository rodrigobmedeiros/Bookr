from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header: str = 'Bookr Administration'


admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)