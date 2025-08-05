from msilib.schema import ListView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View

from books.forms import BookReviewForm
from books.models import Book, BookReview, Author


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

class EditReviewView(View):
    def get(self, request, book_id, review_id):
        comment = get_object_or_404(BookReview, id=review_id)
        book = comment.book
        comments = BookReview.objects.filter(book=book).exclude(id=review_id)

        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this review.")
            return redirect(reverse('books:detail', kwargs={'book_id': book_id}))

        comment_form = BookReviewForm(instance=comment)
        return render(request, 'books/edit_review.html', {'review_form': comment_form, 'book': book, 'comments': comments})

    def post(self, request, book_id, review_id):
        comment = get_object_or_404(BookReview, id=review_id)

        # Check if the user is authorized to edit the comment
        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this review.")
            return redirect(reverse('books:detail', kwargs={'book_id': book_id}))

        comment_form = BookReviewForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Review updated successfully.")
            return redirect(reverse('books:detail', kwargs={'book_id': book_id}))
        else:
            messages.error(request, "Please correct the error below.")

        return render(request, 'books/edit_review.html', {'review_form': comment_form})

class ConfirmationDeleteView(View):
    def get(self, request, book_id, review_id):
        comment = BookReview.objects.get(id=review_id)
        book = Book.objects.get(id=book_id)

        return render(request, 'books/del_con.html', {'book': book, 'review': comment})

class DeleteBookReviewView(View):
    def get(self, request, book_id, review_id):
        review = BookReview.objects.get(id=review_id)
        review.delete()
        return redirect(reverse('books:detail', kwargs={'book_id': book_id}))

class AuthorView(View):

    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)

        context = {
            'author': author,

        }

        return render(request, 'author/author.html', context)

