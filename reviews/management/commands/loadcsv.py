import csv
import re 

from django.contrib.auth.models import User 
from django.core.management.base import BaseCommand, CommandError 
from reviews.models import Publisher, Contributor, Book, BookContributor, Review