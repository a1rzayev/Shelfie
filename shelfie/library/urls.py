from django.urls import path
from . import views
import django.contrib.auth.views as djviews

urlpatterns = [
    path('', views.main_menu, name='home'),
    path('main-menu/', views.main_menu, name='main_menu'),
    path('login/', djviews.LoginView.as_view(), name='login'),
    path('logout/', djviews.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('writer-dashboard/', views.writer_dashboard, name='writer_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
]
