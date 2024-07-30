from django.urls import path 
from . import views

urlpatterns = [
    path('',views.SuperUser.as_view(), name='superuser'),
    path('verification/',views.Verification.as_view(), name='verification'),
    path('dashboard/',views.Dashboard.as_view(), name='dashboard')
]
