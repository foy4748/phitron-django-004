from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .forms import AddBookForm
from book.models import Book


# Create your views here.
class ShowAddBookForm(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBookForm
    success_url = "/"
