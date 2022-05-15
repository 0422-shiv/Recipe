from django.shortcuts import render
from django.views import generic
from dashboard.models import Recipe,Categories
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "home.html"  
    context_object_name  = 'recipes'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['recipes']=Recipe.objects.filter(status=True)
       
        return context