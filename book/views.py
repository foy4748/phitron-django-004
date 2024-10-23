from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, View
from django.contrib import messages
from django.shortcuts import render


# from utils.send_email import success_email

from .forms import AddBookForm, AddCategoryForm, AddReviewForm
from book.models import Book, BookReview, BorrowedBook, Category


# Create your views here.
class ShowCategoryForm(LoginRequiredMixin, CreateView):
    model = Category
    form_class = AddCategoryForm
    success_url = "/"


class ShowAddBookForm(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBookForm
    success_url = "/"


# class ShowBookList(LoginRequiredMixin, ListView):
#     model = Book

#     def get_queryset(self):
#         q = super().get_queryset()
#         category_id = self.request.GET.get("category_id")

#         # is_filtered = False
#         # category = None

#         if category_id is None:
#             book_list = Book.objects.all()
#             return book_list
#         else:
#             category = Category.objects.get(id=category_id)
#             book_list = Book.objects.filter(category=category)
#             # is_filtered = True
#             return book_list


class ShowBookAndCategoryList(View):
    def get(self, req):
        category_list = Category.objects.all()
        category_id = self.request.GET.get("category_id")

        is_filtered = False
        category = None

        if category_id is None:
            book_list = Book.objects.all()
        else:
            category = Category.objects.get(id=category_id)
            book_list = Book.objects.filter(category=category)
            is_filtered = True

        ctx = {
            "book_list": book_list,
            "category_list": category_list,
            "is_filtered": is_filtered,
            "category": category,
        }
        return render(req, "book/book_list.html", context=ctx)


class ShowBookDetail(LoginRequiredMixin, DetailView):
    model = Book

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        pk = self.kwargs.get("pk")
        book = Book.objects.get(pk=pk)
        if book is not None:
            reviews = BookReview.objects.filter(book=book)
            ctx["review_list"] = reviews
        return ctx


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
                nextUrl = reverse("book:borrowedbook_list")
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
                # Success Toast
                success_message = f"Borrowed book successfully : {book.book_name} | {book.author} by you ({self.request.user.username})"
                messages.success(req, success_message)

                # Success Email
                nextUrl = reverse("book:borrowedbook_list")
                # subject = "Borrowed Book Successfully"
                # success_email(self.request, subject, success_message, nextUrl)
                nextUrl = reverse("book:borrowedbook_list")
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


# Review a Book
class ReviewBook(LoginRequiredMixin, CreateView):
    model = BookReview
    form_class = AddReviewForm
    success_url = reverse_lazy("book:borrowedbook_list")

    def dispatch(self, request, *args, **kwargs):
        book_id = self.kwargs.get("pk")
        book = Book.objects.get(pk=book_id)
        user = request.user

        isBookOK = book is not None
        isBorrwed = BorrowedBook.objects.filter(book=book, user=user).exists()

        # Check if the user has borrowed the book
        if isBookOK is False or isBorrwed is False:
            error_message = f"Book was not borrowed"
            messages.error(self.request, error_message)
            url = reverse_lazy("book:borrowedbook_list")
            # Redirect to an error page or any other page
            return HttpResponseRedirect(url)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        book_id = self.kwargs.get("pk")
        book = Book.objects.get(pk=book_id)
        form.instance.user = self.request.user
        form.instance.book = book
        form.save()
        return super().form_valid(form)
