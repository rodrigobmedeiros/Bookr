from django.template.response import TemplateResponse
from django.contrib import admin
from django.urls  import path

# Register your models here.
class BookrAdminCustom(admin.AdminSite):
    site_header:str = 'Bookr Administration'
    logout_template:str = 'admin/logout.html'

    def get_urls(self):
        # get all predefined urls.
        base_urls = super().get_urls()

        url_patterns = [
            path("admin_profile", self.admin_view(self.profile_view)),  
        ] + base_urls

        # put everything together to return as a complete list os urls patterns.
        return url_patterns

    # example method to create a custom view to admin site
    def profile_view(self, request):
        request.current_app = self.name 
        context = self.each_context(request)

        return TemplateResponse(request, "admin/admin_profile.html", context=context)