from django import forms
from .models import Publisher

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