from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth.decorators import login_required
from .forms import BookForm

from django.contrib.gis.geos import Point
from location_tools.object import nom

from .models import *


radius = 20

# Create your views here.

@login_required
def book_listing(request, *args, **kwargs):
    book_owner = BookOwner.objects.get(user=request.user)
    nearby_books = Book.objects.annotate(distance=Distance(
        'location', request.user.bookowner.location)).order_by('distance')[0:10]
    context = {
        'nearby_books': nearby_books,
        'book_owner': book_owner
    }
    return render(request, 'books_listing.html', context)


def book_detail(request, *args, **kwargs):
    return render(request, 'book-detail.html')

def members_listing(request, *args, **kwargs):
    nearby_members = BookOwner.objects.annotate(distance=Distance(
        'location', request.user.bookowner.location)).order_by('distance')[0:10]
    book_owner = BookOwner.objects.get(user=request.user)
    nearby_books = Book.objects.annotate(distance=Distance(
        'location', request.user.bookowner.location)).order_by('distance')[0:10]
    context = {
        'nearby_members': nearby_members,
        'book_owner': book_owner,
        'nearby_books': nearby_books
    }
    return render(request, 'members_listing.html', context)


def member_detail(request, *args, **kwargs):
    return render(request, 'member-detail.html')

def book_search(request, *args, **kwargs):
    return render(request, 'book-search.html')

def add_book(request, *args, **kwargs):
    return render(request, 'add-book.html')

def contact_us(request, *args, **kwargs):
    return render(request, 'contact-us.html')



def post_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        # get the location from the form
        location = request.POST.get('location')
        print(location)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user.bookowner
            book.save()
            return redirect('books:book_list')
        
        else:
            print(form.errors)
            context = {
                'form': form
            }
            return render(request, 'add-book.html', context)
    else:
        form = BookForm()
        context = {
            'form': form
        }
    return render(request, 'add-book.html', context)

        
        