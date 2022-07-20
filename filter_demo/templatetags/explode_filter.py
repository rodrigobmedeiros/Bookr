from typing import List
from django import template

register = template.Library()

@register.filter
def explode(value: str, separator: str):

    return value.split(separator)