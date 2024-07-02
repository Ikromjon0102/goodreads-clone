from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewDetailSerializer
from books.models import BookReview



class BookReviewDetailAPIView(APIView):
    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewDetailSerializer(book_review)
        return Response(serializer.data)


class BookreviewListAPIView(APIView):
    def get(self, request):
        book_reviews = BookReview.objects.all()
        serializer = BookReviewDetailSerializer(book_reviews, many=True)
        return Response(serializer.data)



# class BookReviewDetailAPIView(View):
#     def get(self, request, id):
#         book_review = BookReview.objects.get(id=id)
#
#         json_data = {
#             'id': book_review.id,
#             'comment': book_review.comment,
#             'stars_given' : book_review.stars_given,
#             'created_at': book_review.created_at,
#
#             'book': {
#                 'id': book_review.book.id,
#                 'title': book_review.book.title,
#                 'description': book_review.book.description,
#                 'isbn': book_review.book.isbn,
#                 'cover_picture': book_review.book.cover_picture.url,
#             },
#
#             'user': {
#                 'id': book_review.user.id,
#                 'username': book_review.user.username,
#                 'first_name': book_review.user.first_name,
#                 'last_name': book_review.user.last_name,
#                 'email': book_review.user.email,
#             }
#
#         }
#         return JsonResponse(json_data)