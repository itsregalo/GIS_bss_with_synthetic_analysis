from django.shortcuts import render
from .models import *
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth.decorators import login_required

radius = 20

# Create your views here.

@login_required
def book_listing(request, *args, **kwargs):
    book_owner = BookOwner.objects.get(user=request.user)
    nearby_books = Book.objects.annotate(distance=Distance('location', request.user.bookowner.location)).order_by('distance')[0:10]
    context = {
        'nearby_books': nearby_books,
        'book_owner': book_owner
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
