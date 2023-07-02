from django.urls import path
from . import views as views


urlpatterns = [
    path('list/',views.employ_list,name='employ_list'),
    path('<int:id>/', views.employ_post_detail, name='employ_post_detail'),
    path('create/', views.create_employ_post, name='create_employ_post'),
    path('<int:id>/update/',views.update_employ_post,name='update_employ_post'),
    path('<int:id>/delete/',views.delete_employ_post,name='delete_employ_post'),-


    path('create/', views.create_employ_free_post, name='create_employ_free_post'),
    path('<int:id>/update/',views.update_employ_free_post,name='update_employ_free_post'),
    path('<int:id>/delete/',views.delete_employ_free_post,name='delete_employ_free_post'),
    path('',views.detail_qna,name='detail_qna'),
    path('', views.create_question, name='create_question'),
    path('',views.delete_question,name='delete_question'),
    path('', views.create_answer, name='create_answer'),
    path('',views.delete_answer,name='delete_answer'),







]