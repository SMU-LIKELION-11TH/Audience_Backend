from django.urls import path
from . import views as views


urlpatterns = [
    path('<int:post_id>/<str:category>/', views.employ_post_detail, name='employ_post_detail'),
#     path('create/', views.create_employ_post, name='create_employ_post'),
#     path('<int:id>/update/',views.update_employ_post,name='update_employ_post'),
#     path('<int:id>/delete/',views.delete_employ_post,name='delete_employ_post'),-
#
#
#     path('create/', views.create_employ_free_post, name='create_employ_free_post'),
#     path('<int:id>/update/',views.update_employ_free_post,name='update_employ_free_post'),
#     path('<int:id>/delete/',views.delete_employ_free_post,name='delete_employ_free_post'),
#     path('',views.detail_qna,name='detail_qna'),
    path("question/list/", views.QA_list, name = "QA_list"),
#     path('', views.create_question, name='create_question'),
#     path('',views.delete_question,name='delete_question'),
#     path('', views.create_answer, name='create_answer'),
#     path('',views.delete_answer,name='delete_answer'),
]
