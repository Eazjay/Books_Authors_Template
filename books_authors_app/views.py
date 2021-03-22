from django.shortcuts import render, redirect
from .models import *


def books_index(request):
    context = {
        "headings": ["ID", "Title", "Action"],
        "all_books": Book.objects.all(),
    }
    return render(request, 'books.html', context)


def authors_index(request):
    context = {
        "headings": ["ID", "Name", "Notes", "Action"],
        "all_authors": Author.objects.all(),
    }
    return render(request, 'authors.html', context)


def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/books')

def add_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST["notes"])
    return redirect('/authors')


def add_author_to_book(request):
    book = Book.objects.get(id=int(request.POST['book_id']))
    author = Author.objects.get(id=int(request.POST['author_id']))
    book.authors.add(author)
    return redirect(f'/display_books/{book.id}')

def add_book_to_author(request):
    book = Book.objects.get(id=int(request.POST['book_id']))
    author = Author.objects.get(id=int(request.POST['author_id']))
    author.books.add(book)
    return redirect(f'/display_authors/{author.id}')

def display_books(request, book_id):
    context = {
        "this_book": Book.objects.get(id=book_id),
        "all_authors": Author.objects.all(),
    }
    return render(request, 'displayBooks.html', context)

def display_authors(request, author_id):
    context = {
        "this_author": Author.objects.get(id=author_id),
        "all_books": Book.objects.all(),
    }
    return render(request, 'displayAuthors.html', context)
