from django.shortcuts import render
from .utils import average_rating
from .models import Book


def book_list(request):

    books = Book.objects.all()
    book_list = []

    for book in books:

        reviews = book.review_set.all()
        
        if reviews:
            book_rating = average_rating([
                review.rating 
                for review in reviews
            ])
        else:
            book_rating = None

        number_of_reviews = len(reviews)

        book_list.append(
            {
                'book': book, 
                'book_rating': book_rating,
                'number_of_reviews': number_of_reviews
            }
        )

    context = {'book_list': book_list}

    return render(request, 'reviews/book_list.html', context=context)

def teste(request):

    return render(request, 'reviews/example_bootstrap.html')