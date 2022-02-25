import csv
import re 

from django.contrib.auth.models import User 
from django.core.management.base import BaseCommand, CommandError 
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class Command(BaseCommand):
    help = 'Load the reviews data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('--csv', type=str)