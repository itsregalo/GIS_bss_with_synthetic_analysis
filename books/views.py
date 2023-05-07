from django.shortcuts import render
from .models import *
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

radius = 20

# Create your views here.

def book_listing(request, *args, **kwargs):
    nearby_books = Book.objects.annotate(distance=Distance('location', request.user.bookowner.location)).filter(distance__lte=radius)
    context = {
        'nearby_books': nearby_books
    }
    return render(request, 'books_listing.html', context)

def book_detail(request, *args, **kwargs):
    return render(request, 'book-detail.html')

def members_listing(request, *args, **kwargs):
    nearby_members = BookOwner.objects.filter(location__distance_lte=(request.user.bookowner.location, Distance(km=radius)))
    context = {
        'nearby_members': nearby_members
    }
    return render(request, 'members_listing.html', context)
