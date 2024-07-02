from django.urls import path

from api.views import BookReviewDetailAPIView, BookreviewListAPIView

app_name = 'api'
urlpatterns = [
    path('reviews/', BookreviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(), name='review-detail'),
]