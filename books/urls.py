
from django.urls import path
from books.views import BookListView, BookDetailView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
]
