from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('post/<int:pk>/', views.current_post, name='current_post'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('profile/id<int:user_id>', views.profile, name='profile'),
    path('profile/id<int:user_id>/posts', views.profile_posts, name='profile_posts'),
    path('profile/new', views.register, name='register'),
]
