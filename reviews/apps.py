from django.contrib.admin import apps
from django.apps import AppConfig

class ReviewsConfig(AppConfig):
    name = 'reviews'

class ReviewsAdminConfig(apps.AdminConfig):
    default_site = 'admin.BookrAdminSite'