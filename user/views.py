from django.shortcuts import render
from django.views import generic
# Create your views here.


class LoginView(generic.TemplateView):
    template_name = "login.html"  
    
class RegisterView(generic.TemplateView):
    template_name = "register.html"  