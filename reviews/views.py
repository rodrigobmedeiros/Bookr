from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    name = request.GET.get('name') or 'World'

    return render(request, 'base.html')