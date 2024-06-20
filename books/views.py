from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from books.forms import BookReviewForm
from books.models import Book, BookReview


# class BookListView(ListView):
#     model = Book
#     template_name = 'books/book_list.html'
#     context_object_name = 'books'
#     paginate_by = 4




class BookListView(View):
    def get(self, request):
        books = Book.objects.all()

        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 3)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {"page_obj": page_obj,}
        return render(request, 'books/list.html', context)

# class BookDetailView(View):
#     def get(self, request, book_id):
#         book = Book.objects.get(pk=book_id)
#
#         context = {'book': book}
#         return render(request, 'books/detail.html', context)

class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        review_form = BookReviewForm()
        context = {
            "book": book,
            "review_form": review_form
        }
        return render(request, "books/detail.html", context)

class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user = request.user,
                stars_given = review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment'],
            )
            return redirect(reverse('books:detail', kwargs={'book_id': book.id}))

        context = {
            "book": book,
            "review_form": review_form
        }
        return render(request, "books/detail.html", context)

class DeleteBookReviewView(View):
    def get(self, request, book_id, review_id):
        review = BookReview.objects.filter(id=review_id)
        review.delete()
        return redirect(reverse('books:detail', kwargs={'book_id': book_id}))
