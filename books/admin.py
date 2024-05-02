from django.contrib import admin
from .models import Book,BookAuthor ,Author ,BookReview

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'isbn']
    list_display = ['title', 'isbn', 'description']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'bio']

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['stars_given', 'book', 'user']
    list_filter = ['user', 'stars_given']

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['book', 'author']
    list_filter = ['author']

admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)