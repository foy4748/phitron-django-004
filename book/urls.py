from django.urls import path

from book.views import (
    BorrowBook,
    ReturnBook,
    ShowAddBookForm,
    ShowBookList,
    ShowBookDetail,
    ShowBorrowedBookList,
)

app_name = "book"

urlpatterns = [
    # Reload Browser URL config
    path("add-book/", ShowAddBookForm.as_view(), name="book_form"),
    path("book-list/", ShowBookList.as_view(), name="book_list"),
    path("book-detail/<str:pk>", ShowBookDetail.as_view(), name="book_detail"),
    path("borrow-book/<str:pk>", BorrowBook.as_view(), name="borrow_book"),
    path(
        "borrowed-book-list/", ShowBorrowedBookList.as_view(), name="borrowedbook_list"
    ),
    path("return-borrowed-book/<str:pk>", ReturnBook.as_view(), name="return_book"),
]
