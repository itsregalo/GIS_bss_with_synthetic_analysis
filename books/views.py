from django.shortcuts import render

# Create your views here.

def book_listing(request, *args, **kwargs):
    return render(request, 'books_listing.html')
