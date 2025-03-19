from django.urls import path
from rest_framework.routers import DefaultRouter

# from api.views import BookReviewDetailAPIView, BookreviewListAPIView

from api.views import BookReviewAPIViewset

app_name = 'api'

router = DefaultRouter()
router.register('reviews', BookReviewAPIViewset, basename='review')
urlpatterns = router.urls



# app_name = 'api'
# urlpatterns = [
#     path('reviews/', BookreviewListAPIView.as_view(), name='review-list'),
#     path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(), name='review-detail'),
# ]