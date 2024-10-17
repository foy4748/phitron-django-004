from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView

from .forms import AddBookForm
from book.models import Book


# Create your views here.
class ShowAddBookForm(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBookForm
    success_url = "/"


class ShoowBookList(LoginRequiredMixin, ListView):
    model = Book


class ShoowBookDetail(LoginRequiredMixin, DetailView):
    model = Book
