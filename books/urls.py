from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', book_listing, name='book_list'),
    path('book-members/', members_listing, name='members_list'),
    path('book-upload/', post_book, name='add_book'),
]