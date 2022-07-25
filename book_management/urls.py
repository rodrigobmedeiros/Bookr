"""bookr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    BookDeleteView, 
    BookRecordFormView, 
    BookUpdateView, 
    FormSuccessView, 
    FormDeleteView, 
    BookCreateView
)

urlpatterns = [
    path('', BookRecordFormView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('delete_success', FormDeleteView.as_view(), name='form_delete'),
    path('book_record_create', BookCreateView.as_view(), name='book_create'),
    path('book_record_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book_record_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete')
]