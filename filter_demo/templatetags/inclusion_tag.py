from django import template 

register = template.Library()

@register.inclusion_tag('book_list.html')
def book_list(books):

    books_names = [
        book_name 
        for book_name, book_author in books.items()
    ]

    return {'book_list': books_names}