from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.User.as_view(), name='user'),
    path('verification/', views.UserVerification.as_view(), name='userverification'),
    path('<username>/dashboard/', views.UserDashboard.as_view(), name='userdashboard'),
]
