from django.urls import path
from . import views as views


urlpatterns = [
    path('list/',views.job_list,name='job_list'),
    path('<int:id>/', views.job_post_detail, name='job_post_detail'),
    path('create/', views.create_job_post, name='create_job_post'),
    path('<int:id>/update/',views.update_job_post,name='update_job_post'),
    path('<int:id>/delete/',views.delete_job_post,name='delete_job_post'),

    path('', views.create_job_free_post, name='create_job_free_post'),
    path('', views.update_job_free_post, name='update_job_free_post'),
    path('', views.delete_job_free_post, name='delete_job_free_post'),
    path('',views.report,name='report'),


]