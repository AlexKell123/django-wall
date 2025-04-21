from django.contrib import admin
from django.urls import path, include

from django_wall.views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('wall/', include('wall.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
