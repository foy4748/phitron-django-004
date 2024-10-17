from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, View
from django.contrib import messages

from .forms import AddBookForm
from book.models import Book, BorrowedBook


# Create your views here.
class ShowAddBookForm(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBookForm
    success_url = "/"


class ShowBookList(LoginRequiredMixin, ListView):
    model = Book


class ShowBookDetail(LoginRequiredMixin, DetailView):
    model = Book


class ShowBorrowedBookList(LoginRequiredMixin, ListView):
    model = BorrowedBook

    def get_queryset(self):
        return BorrowedBook.objects.filter(user=self.request.user).order_by(
            "-borrowedAt"
        )


# Borrow a book
class BorrowBook(LoginRequiredMixin, View):
    def get(self, req, *_, **kwargs):
        try:
            pk = kwargs.get("pk")
            book = Book.objects.get(pk=pk)
            user = req.user
            bookOK = book is not None
            userOK = user is not None
            balanceOK = user.profile.balance - book.price >= 0
            quantityOK = book.quantity - 1 >= 0

            if quantityOK is False:
                error_message = f"Book is out of stock"
                messages.error(req, error_message)
                nextUrl = reverse("book:book_list")
                return HttpResponseRedirect(nextUrl)

            if balanceOK is False:
                error_message = f"Balance is NOT sufficient"
                messages.error(req, error_message)
                nextUrl = reverse("book:book_list")
                return HttpResponseRedirect(nextUrl)

            if bookOK and userOK:
                book.quantity = book.quantity - 1
                user.profile.balance = user.profile.balance - book.price
                book.save()  # Quantity Updated
                user.profile.save()  # Balance Updated
                borrow_instance = BorrowedBook(user=user, book=book)
                borrow_instance.save()
                print(borrow_instance)
                success_message = (
                    f"Borrowed book successfully : {book.book_name} | {book.author}"
                )
                messages.success(req, success_message)
                nextUrl = reverse("book:book_list")
                return HttpResponseRedirect(nextUrl)
            else:
                error_message = f"Non-existing Book or User"
                messages.error(req, error_message)
                nextUrl = reverse("book:book_list")
                return HttpResponseRedirect(nextUrl)
        except IntegrityError:
            error_message = f"Already Borrowed"
            messages.error(req, error_message)
            nextUrl = reverse("book:book_list")
            return HttpResponseRedirect(nextUrl)


# Return a book
class ReturnBook(LoginRequiredMixin, View):
    def get(self, req, *_, **kwargs):
        pk = kwargs.get("pk")
        borrow_instance = BorrowedBook.objects.get(pk=pk)
        print(borrow_instance)
        book = Book.objects.get(pk=borrow_instance.book.id)
        user = req.user
        bookOK = book is not None
        userOK = user is not None

        if bookOK and userOK:
            book.quantity = book.quantity + 1
            user.profile.balance = user.profile.balance + book.price
            book.save()  # Quantity Updated
            user.profile.save()  # Balance Updated
            borrow_instance.delete()  # Deleting Borrowing Record
            print(borrow_instance)
            success_message = (
                f"RETURNED Book successfully : {book.book_name} | {book.author}"
            )
            messages.success(req, success_message)
            nextUrl = reverse("book:book_list")
            return HttpResponseRedirect(nextUrl)
        else:
            error_message = f"Non-existing Borrowed Book or User"
            messages.error(req, error_message)
            nextUrl = reverse("book:book_list")
            return HttpResponseRedirect(nextUrl)
