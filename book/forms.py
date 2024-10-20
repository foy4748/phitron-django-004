from django import forms

from book.models import Book, BookReview, Category


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("createdAt",)


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ["review"]
