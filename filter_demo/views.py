from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request):
    names = "john,doe,mark,swain"
    return render(request, "index.html", {'names': names})

def greeting_view(request: HttpRequest):

    context = {
        'username': request.user.username
    }
    return render(request, "simples_tag_template.html", context=context)

def book_list(request: HttpRequest):

    books = {
        "The night rider": "Ben Author",
        "The Justice": "Don Abeman"
    }

    context = {
        "username": request.user.username,
        "books": books
    }

    return render(request, 'inclusion_tag_template.html', context=context)