import re
from django.shortcuts import render 

def profile(request):

    return render(request, template_name='profile.html')