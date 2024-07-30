from django.shortcuts import render, redirect
from django.views import generic

from .models import SuperUser


# Create your views here.
class SuperUser(generic.TemplateView):
    
    def get(_self ,request):
        return render(request,'superuser\index.html')
    
    def post(_self, request):
        email = request.POST.get('email')
        print(email)
        context = {email: email}
        request.session['email'] = email
        try:
            # user = SuperUser.objects.create(email=email)
            # user.save()
            # print(user)
            return redirect('/verification/')
        except Exception as e:
            print (e)
            return redirect('/')

        


class Verification(generic.TemplateView):
    
    def get(_self ,request):
        return render(request,'superuser\pages\otp.html')
    
    # def post(_self, request):
    #     email = req.POST.get('email')
    #     print(email)
    #     context = {email: email}
    #     request.session['email'] = email
    #     return redirect('/verification/')



class Dashboard(generic.TemplateView):

    def get(_self, request):
        return render(request, 'superuser\pages\dashboard.html')