from django.db import models
from accounts.models import User
import uuid

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.PointField()
    slug = models.SlugField(max_length=200, unique=True)
    uuid = models.UUIDField(unique=True, editable=False)

    class Meta:
        ordering = ['title']
        db_table = 'book'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()

        return super(Book, self).save(*args, **kwargs)
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment_score = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'review'

    def __str__(self):
        return self.comment

class BorrowRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'borrow_request'

    def __str__(self):
        return self.book.title
    
class LendRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lender = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'lend_request'

    def __str__(self):
        return self.book.title
        