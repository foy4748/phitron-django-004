from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=1024)

    def __str__(self):
        return self.category


class Book(models.Model):
    book_name = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    book_image = models.ImageField(upload_to="book/uploads/", blank=True, null=True)
    description = models.TextField(max_length=5120)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_name


class BorrowedBook(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="borrowed_books"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="borrowed_books"
    )
    borrowedAt = models.DateTimeField(default=timezone.now)
    balance_after_borrowing = models.DecimalField(
        decimal_places=2, max_digits=12, default=0.00
    )

    class Meta:
        unique_together = (("book", "user"),)

    def __str__(self):
        return f"{self.book.book_name} is borrowed by {self.user.first_name} {self.user.last_name}"


class BookReview(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reviewed_books"
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="reviewed_books"
    )
    review = models.TextField(max_length=5120)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.book.book_name} || {self.review}"
