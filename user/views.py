from django.shortcuts import render
from django.views import generic
# Create your views here.

class User(generic.TemplateView):

    def get(_self, request):
        return render(request, 'user\index.html')

class UserVerification(generic.TemplateView):

    def get(_self, request):
        return render(request, 'user\pages\otp.html')

class UserDashboard(generic.TemplateView):

    def get(_self, request):
        return render(request, 'user\pages\dashboard.html')