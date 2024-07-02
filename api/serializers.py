from rest_framework import serializers

from books.models import BookReview, Book
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description','isbn','cover_picture']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class BookReviewDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = BookReview
        fields = ['id', 'stars_given', 'comment', 'book', 'user']