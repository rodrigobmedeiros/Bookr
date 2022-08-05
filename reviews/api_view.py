from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

@api_view(['GET'])
def first_api_view(request):
    
    books_into_database = Book.objects.count()

    return Response({'books_count': books_into_database})