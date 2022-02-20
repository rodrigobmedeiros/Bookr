from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    name = request.GET.get('name') or 'World'

    context = {
        'name': name
    }

    return render(request, 'base.html', context)