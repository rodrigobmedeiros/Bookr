from django.contrib.auth.models import User 
from django.utils import timezone 
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied 

from .models import Book, Publisher, Review, Contributor, BookContributor
from .utils import average_rating

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
            'publisher',
            'reviews',
            'rating'
        ]

class BookContributorSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    
    class Meta:
        model = BookContributor
        fields = [
            'book',
            'role'
        ]
        

class ContributorSerializer(serializers.ModelSerializer):

    contributions = BookContributorSerializer(source='bookcontributor_set', many=True)

    class Meta:
        model = Contributor
        fields = [
            'first_names',
            'last_names',
            'email',
            'number_of_contributions',
            'contributions'
        ]
