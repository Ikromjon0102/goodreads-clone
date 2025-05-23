from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import landing_page, home

urlpatterns = [
    path('', landing_page, name = 'landing_page'),
    path('home/', home, name = 'home'),
    path('users/', include('users.urls'), name='users'),
    path('books/', include('books.urls'), name='books'),
    path('api/', include('api.urls'), name='api'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)