from django.shortcuts import render, get_object_or_404
from .utils import average_rating
from .models import Book
from .forms import SearchForm


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
    reviews = book.review_set.all()

    context = {
        'book': book,
        'average_rating': average_rating,
        'number_of_reviews': number_of_reviews,
        'reviews': reviews
    }

    return render(request, 'reviews/book_detail.html', context=context)

def book_search(request):

    
    
    if request.method == 'GET':

        search_form = SearchForm(request.GET)
        title = 'Book Search'
        books = []

        if search_form.is_valid():

            search_text = search_form.cleaned_data.get('search')

            if search_text != '':

                books = Book.objects.filter(title__icontains=search_text)
                title = f'Search Results for "{search_text}"'

        

    context = {
        'form': search_form,
        'books': books,
        'title': title,
    }

    return render(request, 'reviews/book_search.html', context=context)



def main(request):

    return render(request, 'base.html')