from django.shortcuts import render

# Create your views here.

def book_listing(request, *args, **kwargs):
    return render(request, 'books_listing.html')

def book_detail(request, *args, **kwargs):
    return render(request, 'book-detail.html')
