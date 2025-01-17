from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('writer-dashboard/', views.writer_dashboard, name='writer_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
]
