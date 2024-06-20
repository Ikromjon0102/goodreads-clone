
from django.urls import path
from books.views import BookListView, BookDetailView, AddReviewView, DeleteBookReviewView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('<int:book_id>/review/', AddReviewView.as_view(), name='reviews'),
    path('<int:book_id>/<int:review_id>/delete/', DeleteBookReviewView.as_view(), name='delete_review'),
]
