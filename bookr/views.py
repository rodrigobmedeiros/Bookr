import re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):

    return render(request, template_name='profile.html')