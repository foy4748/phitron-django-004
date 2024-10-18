from django import forms

from book.models import Book, BookReview


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("createdAt",)


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ["review"]
