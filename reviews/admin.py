from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class BookAdmin(admin.ModelAdmin):

    # use this list to define fields or methods to be displayed in Admin Site for an especific model.
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    date_hierarchy = 'publication_date'
    search_fields = ('title', 'isbn__exact', 'publisher__name')

    def isbn13(self, obj):
        
        """ 9780316769174 => 978-0-31-676917-4"""

        return (
            f'{obj.isbn[0:3]}-'
            f'{obj.isbn[3:4]}-'
            f'{obj.isbn[4:6]}-'
            f'{obj.isbn[6:12]}-'
            f'{obj.isbn[12:]}'
        )

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Linkage', {'fields': ('creator', 'book')}),
        ('Review content', {'fields': ('content', 'rating')})
    )

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
# By default the register uses the ModelAdmin class.
admin.site.register(Book, admin_class=BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, admin_class=ReviewAdmin)
