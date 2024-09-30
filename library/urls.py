from django.urls import path
from .views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, \
    BookDeleteView

app_name = 'library'

urlpatterns = [
    # path('books_list/', books_list, name='books_list'),
    # path('book_detail/<int:book_id>', book_detail, name='book_detail'),

    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
