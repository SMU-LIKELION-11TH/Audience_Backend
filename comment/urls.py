from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.create_question, name='create_comment'),
    path('', views.delete_question, name='delete_comment'),
    path('', views.create_answer, name='create_reply'),
    path('', views.delete_answer, name='delete_reply'),
]