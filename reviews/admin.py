from django import contrib
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

# Register your models here.
contrib.admin.site.register(Publisher)
contrib.admin.site.register(Contributor)
contrib.admin.site.register(Book)
contrib.admin.site.register(BookContributor)
contrib.admin.site.register(Review)
