import re
from django.contrib import auth
from django.conf import settings
from django.db import models

class Publisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __str__(self):

        return self.name

class Book(models.Model):
    """A published book."""
    title = models.CharField(max_length=70, help_text='The title of the book.')
    publication_date = models.DateField(verbose_name='Date the book was published.')
    isbn = models.CharField(max_length=20, verbose_name='ISBN number of the book.')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    sample = models.FileField(upload_to='book_samples/', null=True, blank=True)

    def __str__(self):

        return self.title

    def average_rating_number_of_reviews(self):

        reviews = self.review_set.all()

        if not reviews:

            return None, 0
        
        book_rating = sum([review.rating for review in reviews]) / len(reviews)

        return round(book_rating), len(reviews)

    def contributors_names(self):

        contributors = self.contributors.all()
        contributors_names = [contributor.complete_name() for contributor in contributors]

        return ', '.join(contributors_names)

class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor, co-author."""
    first_names = models.CharField(max_length=50, help_text="The contributor's first name or names.")
    last_names = models.CharField(max_length=50, help_text="The contributor's last name or names.")
    email = models.EmailField(help_text="The contact email for the contributor.")

    def initialled_name(self):
        """Treatment concatenating contributor's last names with , and initial firt names with upper case."""
        
        initial_first_names = ''.join([
            name[0].upper() for name in self.first_names.split(' ')
        ])

        return ', '.join([self.last_names, initial_first_names])

    def complete_name(self):
        """Treatment concatenating first and last names, configuring the complete name of a contributor."""

        return ' '.join([self.first_names, self.last_names])

    def __str__(self):

        return self.initialled_name()

class BookContributor(models.Model):
    """Estabilish many to many relationship between Books and Contributors"""
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name='The role this contributor had in the book.', 
        choices=ContributionRole.choices, 
        max_length=20
    )

class Review(models.Model):
    """Reviews added by users"""
    content = models.TextField(help_text='The review text.')
    rating = models.IntegerField(help_text='The rating the reviewer has given.')
    date_created = models.DateTimeField(auto_now=True, help_text='The date and time the review was created.')
    date_edited = models.DateTimeField(null=True, help_text='The date and time the review was last edited.')
    creator =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text='The Bok that tis review is for.')