from django.urls import path

from book.views import BorrowBook, ShowAddBookForm, ShowBookList, ShowBookDetail

app_name = "book"

urlpatterns = [
    # Reload Browser URL config
    path("add-book/", ShowAddBookForm.as_view(), name="book_form"),
    path("book-list/", ShowBookList.as_view(), name="book_list"),
    path("book-detail/<str:pk>", ShowBookDetail.as_view(), name="book_detail"),
    path("borrow-book/<str:pk>", BorrowBook.as_view(), name="borrow_book"),
]
