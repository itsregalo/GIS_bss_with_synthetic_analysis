from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth.decorators import login_required
from .forms import BookForm

from django.contrib.gis.geos import Point
from location_tools.object import nom
from .forms import BookForm, BookReviewSentimentForm

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


def category_books(request, category_slug, *args, **kwargs):
    category = BookCategory.objects.get(slug=category_slug)
    books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'books': books
    }
    return render(request, 'category-books.html', context)


def book_detail(request, book_id, *args, **kwargs):
    book = Book.objects.get(id=book_id)
    book_owner = BookOwner.objects.get(user=request.user)

    book_distance_from_user = book.location.distance(
        request.user.bookowner.location) * 100
    book_distance_from_user = round(book_distance_from_user, 2) 

    try:
        location_name = nom.reverse((book.location.y, book.location.x))
    except:
        location_name = "Name Not Available"

    context = {
        'book': book,
        'book_owner': book_owner,
        'book_distance_from_user': book_distance_from_user,
        'location_name': location_name
    }
    return render(request, 'book-detail.html', context)

@login_required
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


def member_books(request, member_id, *args, **kwargs):
    member = BookOwner.objects.get(id=member_id)
    member_books = Book.objects.filter(owner=member)
    context = {
        'book_owner': member,
        'nearby_books': member_books
    }
    return render(request, 'member-books.html', context)

def book_search(request, *args, **kwargs):
    return render(request, 'book-search.html')

def add_book(request, *args, **kwargs):
    return render(request, 'add-book.html')

def contact_us(request, *args, **kwargs):
    return render(request, 'contact-us.html')


@login_required
def post_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        # get the location from the form
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user.bookowner
            book.location = Point(float(longitude), float(latitude))
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


def post_review(request, book_id):
    if request.method == 'POST':
        form = BookReviewSentimentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = Book.objects.get(id=book_id)
            review.user = request.user
            review.save()
            return redirect('books:book_detail', book_id=book_id)
        else:
            print(form.errors)
            context = {
                'form': form
            }
            return render(request, 'book-detail.html', context)
    else:
        form = BookReviewSentimentForm()
        context = {
            'form': form
        }
    return render(request, 'book-detail.html', context)
        