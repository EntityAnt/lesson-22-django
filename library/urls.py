from django.urls import path
from .views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, \
    BookDeleteView, AuthorListView, AuthorCreateView, AuthorUpdateView, ReviewBookView, RecommendBookView

app_name = 'library'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_update'),

    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/recommend/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/<int:pk>/review/', ReviewBookView.as_view(), name='book_review'),
]
