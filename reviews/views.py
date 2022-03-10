from django.shortcuts import render, get_object_or_404
from .utils import average_rating
from .models import Book


def book_list(request):

    books = Book.objects.all()
    book_list = []

    for book in books:

        reviews = book.review_set.all()
        average_rating, number_of_reviews = book.average_rating_number_of_reviews()

        book_list.append(
            {
                'book': book, 
                'book_rating': average_rating,
                'number_of_reviews': number_of_reviews
            }
        )

    context = {'book_list': book_list}

    return render(request, 'reviews/book_list.html', context=context)

def book_detail(request, id):

    book = get_object_or_404(Book, pk=id)
    average_rating, number_of_reviews = book.average_rating_number_of_reviews()

    context = {
        'book': book,
        'average_rating': average_rating,
        'number_of_reviews': number_of_reviews
    }

    return render(request, 'reviews/book_detail.html', context=context)