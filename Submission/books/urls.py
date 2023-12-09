from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', book_listing, name='book_list'),
    path('book-detail/<int:book_id>/', book_detail, name='book_detail'),
    path('book-members/', members_listing, name='members_list'),
    path('book-upload/', post_book, name='add_book'),
    path('member-books/<int:member_id>/', member_books, name='member_books'),
    path('category-books/<slug:category_slug>/', category_books, name='category_books'),
]