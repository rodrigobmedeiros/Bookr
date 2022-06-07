from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.files.images import ImageFile
from .models import Book, Contributor, Publisher, Review
from .forms import SearchForm, PublisherForm, ReviewForm, BookMediaForm
from PIL import Image
from io import BytesIO

def is_staff_user(user):
    return user.is_staff

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

@user_passes_test(is_staff_user)
def publisher_edit(request, pk=None):

    if pk is not None:

        publisher = get_object_or_404(Publisher, pk=pk)
    
    else:

        publisher = None

    if request.method == 'POST':

        form = PublisherForm(request.POST, instance=publisher)
        
        if form.is_valid():
        
            updated_publisher = form.save()

            if publisher is None:

                messages.success(request, f'Publisher {updated_publisher} was created!')

            else:

                messages.success(request, f'Publisher {updated_publisher} was updated!')

            return redirect('publisher_edit', updated_publisher.pk)

    else:

        form = PublisherForm(instance=publisher)

    context = {
        'form': form,
        'instance': publisher,
        'model_type': "Publisher"
    }

    return render(request, 'reviews/instance_form.html', context=context)


@login_required
def review_edit(request, book_pk, review_pk=None):

    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review.objects.filter(book=book), pk=review_pk)

        user = request.user

        if not user.is_staff and review.creator.id != user.id:

            raise PermissionDenied


    else:
        review = None

    if request.method == 'POST':

        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():

            updated_review = form.save(commit=False)
            updated_review.book = book 

            if review is not None:

                updated_review.date_edited = now()
                messages.success(request, f'Review for {book.title} was edited!')

            else:
                messages.success(request, f'Review  for {book.title} was created!')
            
            updated_review.save()
            return redirect('book_details', book.pk)

    else:

        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'instance': review,
        'model_type': "Review",
        'related_model_type': "Book",
        'related_instance': book
    }

    return render(request, 'reviews/instance_form.html', context=context)

@login_required
def book_media(request, book_pk):
    
    book = get_object_or_404(Book, pk=book_pk)

    if request.method == 'POST':

        form = BookMediaForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            
            # As I want to resize the image let commit=False.
            book: Book = form.save(commit=False)

            # Open image to manipulate it.
            image = Image.open(book.cover)

            # Resize image considering 300 x 300 pixles maximun value.
            image.thumbnail((300, 300))

            # Use BytesIO to work with "files" in memory before update the model.
            image_data = BytesIO()
            image.save(fp=image_data, format=image.format)
            image_file = ImageFile(image_data)

            # Save updated cover and model
            book.cover.save(book.cover.name, image_file)
            book.save()

            messages.success(request, f'Book {book} was updated!')
            return redirect('book_details', book.pk)

    else:

        form = BookMediaForm(instance=book)

    context = {
        'form': form,
        'instance': book,
        'model_type': "Book",
        'is_file_upload': True
    }

    return render(request, 'reviews/instance_form.html', context=context)