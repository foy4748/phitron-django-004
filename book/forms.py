from django import forms

from book.models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("createdAt",)
