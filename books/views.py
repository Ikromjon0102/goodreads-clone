from django.shortcuts import render
from django.views.generic import View

from books.models import Book

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'books/list.html', context)

class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)

        context = {'book': book}
        return render(request, 'books/detail.html', context)
