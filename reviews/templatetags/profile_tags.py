from django import template
from django.contrib.auth.models import User
from reviews.models import Review
from typing import List

register = template.Library()

@register.inclusion_tag('reviews/read_book_list.html')
def books_list(username: str):
    
    reviews: List[Review] = Review.objects.filter(creator=User.objects.get(username=username))
    books = set(review.book for review in reviews)

    return {'books': list(books)}