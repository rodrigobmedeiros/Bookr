from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from models import Book
from bookr.utils import average_rating

def book_list(request):

    books = Book.objects.all()
    book_list = []

    for book in books:

        reviews = book.review_set.all()

        book_rating = average_rating([
            review.rating 
            for review in reviews
        ])

        number_of_reviews = len(reviews)

        book_list.append(
            {
                'book': book, 
                'book_rating': book_rating,
                'number_of_reviews': number_of_reviews
            }
        )

    context = {'book_list': book_list}

    return render(request, 'reviews.book_list.html')