from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))
        self.assertContains(response, 'No books found.')

    def test_books_list(self):
        Book.objects.create(title = 'Book1', description = 'Description1', isbn='12112')
        Book.objects.create(title = 'Book2', description = 'Description2', isbn='12222')
        Book.objects.create(title = 'Book3', description = 'Description3', isbn='12333')

        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_books_detail(self):
        book = Book.objects.create(title = 'Book1', description = 'Description1', isbn='12112')

        response = self.client.get(reverse('books:detail', kwargs={'book_id': book.pk}))
        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
