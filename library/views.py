from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_date__year__gt=1900)


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')



class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        return context


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/books_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')



#
# def books_list(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'library/books_list.html', context)
#
#
# def book_detail(request, book_id):
#     book = Book.objects.get(id=book_id)
#     context = {'book': book}
#     return render(request, 'library/book_detail.html', context)
