from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def welcome_view(request):

    return render(request, 'base.html')

def index(request):

    return render(request, 'base.html')

def book_search(request):

    search_term = request.GET.get('search')
    context = {'search_term': search_term}

    return render(request, 'search.html', context=context)