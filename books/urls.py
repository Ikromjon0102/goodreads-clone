
from django.urls import path
from books.views import BookListView, BookDetailView, AddReviewView, DeleteBookReviewView, EditReviewView, \
    ConfirmationDeleteView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('<int:book_id>/review/', AddReviewView.as_view(), name='reviews'),
    path('<int:book_id>/<int:review_id>/edit/', EditReviewView.as_view(), name='update_review'),

    path('<int:book_id>/<int:review_id>/delete/', ConfirmationDeleteView.as_view(), name='delete-confirmation-review'),
    path('<int:book_id>/<int:review_id>/', DeleteBookReviewView.as_view(), name='delete_review'),
]
