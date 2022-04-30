from django import forms
from .models import Publisher, Review, Book

SEARCH_CHOICES = (
    ('title', 'title'),
    ('contributor', 'contributor')
)

class SearchForm(forms.Form):

    search = forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(choices=SEARCH_CHOICES, required=False)

class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = "__all__"

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = (
            'date_edited',
            'book'
        )
        widgets = {
            'rating': forms.NumberInput(attrs={'max': 5, 'min': 0})
        }

class BookMediaForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            'cover',
            'sample'
        )