from rest_framework import serializers
from .models import Contributor, Publisher, Book, BookContributor

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
