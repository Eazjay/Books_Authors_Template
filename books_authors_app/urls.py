from django.urls import path
from .import views

urlpatterns = [
    path('books', views.books_index),
    path('authors', views.authors_index),
    path('add_book', views.add_book),
    path('add_author_to_book', views.add_author_to_book),
    path('add_author', views.add_author),
    path('display_books/<int:book_id>', views.display_books),
    path('display_authors/<int:author_id>', views.display_authors),
    path('add_book_to_author', views.add_book_to_author),
]