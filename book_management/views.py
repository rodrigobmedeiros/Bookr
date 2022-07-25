from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import BookForm
from .models import Book


# Create your views here.
class BookRecordFormView(FormView):

    template_name = 'book_form.html'
    form_class = BookForm
    success_url = '/book_management/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):

    def get(self, request, *args,  **Kwargs):
        return HttpResponse("Book record saved successfully")

class FormDeleteView(View):

    def get(self, request, *args,  **Kwargs):
        return HttpResponse("Book record deleted successfully")

class BookCreateView(CreateView):
    model = Book
    fields = [
        'name',
        'author'
    ]
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'


class BookUpdateView(UpdateView):
    model = Book
    fields  = [
        'name',
        'author'
    ]
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete_form.html'
    success_url = '/book_management/delete_success'

class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'