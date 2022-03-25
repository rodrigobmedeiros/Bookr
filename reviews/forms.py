from django import forms

SEARCH_CHOICES = (
    ('title', 'title'),
    ('contributor', 'contributor')
)

class SearchForm(forms.Form):

    search = forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(choices=SEARCH_CHOICES, required=False)