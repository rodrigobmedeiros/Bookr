from rest_framework import serializers
from .models import Contributor, Publisher, Book

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        exclude = ('id',)

class BookSerializer(serializers.ModelSerializer):

    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = [
            'title',
            'publication_date',
            'isbn',
            'publisher'
        ]