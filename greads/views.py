from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book, BookReview,BookAuthor

def landing_page(request):
    return render(request, 'landing_page.html')

def home(request):
    reviews = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size',10)
    paginator = Paginator(reviews, page_size)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {
        'reviews': reviews,
        'page_obj': page_obj
    }

    return render(request, 'home.html', context)