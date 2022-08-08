from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Book, Publisher 
from .serializers import BookSerializer, PublisherSerializer

@api_view(['GET'])
def all_books(request):

    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)

class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
