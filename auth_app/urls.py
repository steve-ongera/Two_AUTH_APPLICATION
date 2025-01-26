from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
]
