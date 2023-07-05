from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:post_id>/create/', views.add_like, name='add_like'),
    path('dislike/<int:post_id>/create/', views.add_dislike, name='add_dislike'),
    path('rating/<int:post_id>/create/', views.add_rating, name='add_rating'),
    path('hashtag/<int:post_id>/create/', views.add_hashtag, name='add_hashtag'),
    path('interest/update/', views.update_interest, name='update_interest'),
]