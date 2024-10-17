from django.urls import path

from book.views import ShowAddBookForm

app_name = "book"

urlpatterns = [
    # Reload Browser URL config
    path("add-book/", ShowAddBookForm.as_view(), name="book_form"),
]
