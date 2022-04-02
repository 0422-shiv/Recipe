from django.shortcuts import render
from django.views import generic
from user.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
from .forms import MyPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
# Create your views here.


class MyProfileView(generic.TemplateView):
    template_name = "my-profile.html" 
     
    def get(self,request) :
        user=User.objects.get(id=self.request.user.id)
        return render(request,self.template_name,{"user":user})
    
    def post(self,request):
      
        fullname= request.POST.get("fullname")
      
        email= request.POST.get("email")
        phone= request.POST.get("phone")
       
        if User.objects.filter(mobile_no=phone).filter(~Q(mobile_no=request.user.mobile_no)).exists():
            messages.error(request, 'Mobile Number Already taken')
            return HttpResponseRedirect(reverse('My-Account:myaccount'))
        if User.objects.filter(email=email).filter(~Q(email=request.user.email)).exists():
            messages.error(request, 'Email Already taken') 
            return HttpResponseRedirect(reverse('My-Account:myaccount'))
        User.objects.filter(id=request.user.id).update(
                                        fullname=fullname,
                                                email=email,
                                                  mobile_no=phone)
        
                                       
        if "img" in request.FILES:
            user=request.user
            if user.img:
                image_path=user.img.path
            
                if os.path.exists(user.img.path):
                    os.remove(image_path)
                    user.img=request.FILES["img"]
                    user.save()
            else:
                user.img=request.FILES["img"]
                user.save()
            
        messages.success(request,"Profile updated successfully")
         
        return HttpResponseRedirect(reverse('dashboad:my_profile_view'))
        
            
    
    
class ChangePasswordView(generic.TemplateView):
    template_name = "change-password.html" 
    def post(self,request):
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Password updated successfully ")
        else:
            messages.error(request, form.errors)
		   
        return HttpResponseRedirect(reverse('dashboad:change_password_view')) 
    
    
class RecipeUploadView(generic.TemplateView):
    template_name = "upload-recipe.html" 
    
    
class MyRecipeView(generic.TemplateView):
    template_name = "my-recipes.html" 