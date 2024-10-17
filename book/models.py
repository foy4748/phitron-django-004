from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024)

    book_image = models.ImageField(upload_to="book/uploads/", blank=True, null=True)
    description = models.TextField(max_length=5120)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_name


class BorrowedBook(models.Model):
    book = models.OneToOneField(
        Book, on_delete=models.CASCADE, related_name="borrowed_books"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="borrowed_books"
    )
    borrowedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.book.book_name} is borrowed by {self.user.first_name} {self.user.last_name}"
