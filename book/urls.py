from django.urls import path

from book.views import ShowAddBookForm, ShoowBookList, ShoowBookDetail

app_name = "book"

urlpatterns = [
    # Reload Browser URL config
    path("add-book/", ShowAddBookForm.as_view(), name="book_form"),
    path("book-list/", ShoowBookList.as_view(), name="book_list"),
    path("book-detail/<str:pk>", ShoowBookDetail.as_view(), name="book_detail"),
]
