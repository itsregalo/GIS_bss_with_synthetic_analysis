from django.contrib import admin
from .models import *


class BookOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city']
    search_fields = ['user__username', 'address', 'city']
    list_filter = ['city']

admin.site.register(BookOwner, BookOwnerAdmin)

class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(BookCategory, BookCategoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'owner', 'location', 'timestamp']
    list_filter = ['category', 'owner__city', 'timestamp']

admin.site.register(Book, BookAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    search_fields = ['book__title', 'user__username']
    list_filter = ['rating', 'created_at']

admin.site.register(Review, ReviewAdmin)

class BorrowRequestAdmin(admin.ModelAdmin):
    list_display = ['book', 'borrower', 'status', 'created_at']
    search_fields = ['book__title', 'borrower__username']
    list_filter = ['status', 'created_at']

admin.site.register(BorrowRequest, BorrowRequestAdmin)

class LendRequestAdmin(admin.ModelAdmin):
    list_display = ['book', 'lender', 'status', 'created_at']
    search_fields = ['book__title', 'lender__username']
    list_filter = ['status', 'created_at']

admin.site.register(LendRequest, LendRequestAdmin)


