from django.shortcuts import render
from django.views import generic
# Create your views here.


class MyProfileView(generic.TemplateView):
    template_name = "my-profile.html"  
    
    
class ChangePasswordView(generic.TemplateView):
    template_name = "change-password.html" 
    
    
class RecipeUploadView(generic.TemplateView):
    template_name = "upload-recipe.html" 
    
    
class MyRecipeView(generic.TemplateView):
    template_name = "my-recipes.html" 