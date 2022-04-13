from telnetlib import SE
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .utils import average_rating
from .models import Book, Contributor
from .forms import SearchForm, PublisherForm


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

    # To start the view, default values were defined for title and books
    title = 'Book Search'
    books = []
    
    # To avoid DRY, search form is defined at this point
    if request.method == 'GET':

        search_form = SearchForm(request.GET)

    elif request.method == 'POST':

        search_form = SearchForm(request.POST)

    # Test if the form is valid
    if search_form.is_valid():

        # Get values need to make searchs
        search_text = search_form.cleaned_data.get('search')
        search_in = search_form.cleaned_data.get('search_in')

        if search_text != '':

            title = f'Search Results for "{search_text}"'

            # Here two cases are covered, when info come from url (GET method).
            # In this case search_in is ''
            # If submit button is clicked from HTML form (POST method), search_in became title or contributor
            if search_in in ['title', '']:

                # Simple query based com title
                books = Book.objects.filter(title__icontains=search_text)

            elif search_in == 'contributor':

                # When contributor is selected, the search is executed based on two fields
                # first_names and last_names, to perform that, django.db.models.Q was used
                # To know more about that go to the link -> https://docs.djangoproject.com/en/4.0/topics/db/queries/#complex-lookups-with-q 
                complex_search_query = Q(first_names__icontains=search_text) | Q(last_names__icontains=search_text)
                contributors = Contributor.objects.filter(complex_search_query)

                # once I have all contributors, It's possible to get all books from them
                _ = [books.extend(contributor.book_set.all()) for contributor in contributors]
                
    context = {
        'form': search_form,
        'books': books,
        'title': title,
    }

    return render(request, 'reviews/book_search.html', context=context)

def main(request):

    return render(request, 'base.html')

def publishers(request, pk):

    form = PublisherForm()

    context = {
        'form': form
    }

    return render(request, 'reviews/publishers.html', context=context)