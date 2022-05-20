from django.http import HttpResponseRedirect
from django.views import generic
from dashboard.models import Recipe,RecipeTips
from .models import ContactUs
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dashboard.models import Categories,Recipe
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "home.html"  
    context_object_name  = 'recipes'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['recipes']=Recipe.objects.filter(status=True)
        context['tips'] = RecipeTips.objects.all().order_by('-id')
        return context
    
    
class ContactUsView(generic.View):

    def post(self, request):
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        text= request.POST.get('text')
        ContactUs.objects.create(name=name,email=email,subject=subject,message=text)
        messages.success(request,"Successfull posted")
        return HttpResponseRedirect(reverse('home:home_view'))
    
    
@method_decorator(login_required(login_url='/user'), name="dispatch")    
class UploadRecipeView(generic.TemplateView):
    template_name = "recipe-upload.html" 
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['categories'] =Categories.objects.all()
        context['tips'] = RecipeTips.objects.all().order_by('-id')
        return context
    
    def post(self,request):
        name= request.POST.get('name')
        photo= request.FILES['photo']
        video= request.FILES['video']
        cat= request.POST.get('category')
        description= request.POST.get('description')
        category=Categories.objects.get(id=cat)
        Recipe.objects.create(name=name,img=photo,video=video,category=category
                              ,description=description,created_by=request.user)
        messages.success(request, "Recipe uploaded successful") 
        return HttpResponseRedirect(reverse('home:upload_recipe_view'))