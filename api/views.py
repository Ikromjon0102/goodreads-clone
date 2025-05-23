from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from api.serializers import BookReviewDetailSerializer
from books.models import BookReview
from rest_framework import generics


class BookReviewAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookReviewDetailSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'id'


class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewDetailSerializer
    queryset = BookReview.objects.all()
    lookup_field = 'id'


    # def get(self, request, id):
    #     book_review = BookReview.objects.get(id=id)
    #     serializer = BookReviewDetailSerializer(book_review)
    #     return Response(serializer.data)
    #
    # def delete(self, request, id):
    #     book_review = BookReview.objects.get(id=id)
    #     book_review.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def put(self, request, id):
    #     book_review = BookReview.objects.get(id=id)
    #     serializer = BookReviewDetailSerializer(instance=book_review, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self, request, id):
    #     book_review = BookReview.objects.get(id=id)
    #     serializer = BookReviewDetailSerializer(instance=book_review, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookreviewListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewDetailSerializer
    queryset = BookReview.objects.all().order_by('-created_at')


    # def get(self, request):
    #     book_reviews = BookReview.objects.all().order_by('-created_at')
    #     paginator = PageNumberPagination()
    #     page_obj = paginator.paginate_queryset(book_reviews, request)
    #     serializer = BookReviewDetailSerializer(page_obj, many=True)
    #     return paginator.get_paginated_response(serializer.data)
    #
    # def post(self, request):
    #     serializer = BookReviewDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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