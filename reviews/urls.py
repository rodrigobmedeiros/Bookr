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
from django.contrib import admin
from django.urls import path, include, re_path
from . import views, api_view

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>', views.book_detail, name='book_details'),
    path('book_search/', views.book_search, name='book_search'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>', views.review_edit, name='review_edit'),
    path('books/<int:book_pk>/media', views.book_media, name='book_media'),
    path('api/book_count/', api_view.first_api_view, name='book_count'),
    path('', views.main, name='main')
]
