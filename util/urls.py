from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:post_id>/create/', views.add_like, name='add_like'),
    path('dislike/<int:post_id>/create/', views.add_dislike, name='add_dislike'),
]