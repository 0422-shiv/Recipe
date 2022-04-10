from django.shortcuts import render
from django.views import generic
from dashboard.models import Recipe
# Create your views here.


class FindRecipeView(generic.ListView):
    template_name = "find-recipe.html"  
    context_object_name  = 'recipes'
    def get_queryset(self):
        print(Recipe.objects.filter(status=True))
        return Recipe.objects.filter(status=True)
    