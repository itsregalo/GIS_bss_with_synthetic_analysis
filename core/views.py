from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book, BookOwner
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# Create your views here.
radius = 20

def index(request):
    latest_books = Book.objects.order_by('-timestamp')[:8]
    if request.user.is_authenticated:
        book_owner = BookOwner.objects.get(user=request.user)
        nearby_books = Book.objects.annotate(distance=Distance('location', book_owner.location)).order_by('distance')[0:10]
    else:
        # choose random 6 books
        nearby_books = Book.objects.order_by('?')[:6]
    context = {
        'latest_books': latest_books,
        'nearby_books': nearby_books,
    }
    return render(request, 'index.html', context)