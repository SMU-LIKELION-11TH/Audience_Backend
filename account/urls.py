from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='account_login'),
    path('applicant/create/', views.ApplicantCreateView.as_view(), name='applicant_create'),
    path('employer/create/', views.EmployerCreateView.as_view(), name='employer_create'),
    path('email/search/', views.search_email, name='search_email'),
    path('password/search/', views.search_password, name='search_password'),
    path('detail/', views.account_detail, name='account_detail'),
    path('password/check/', views.check_password, name='check_password'),
    path('password/update/', views.change_password, name='change_password'),
    path('update/', views.AccountUpdateView.as_view(), name='account_update'),
]
