from django.shortcuts import render
from django.views import generic
from dashboard.models import Recipe,Categories
# Create your views here.


class FindRecipeView(generic.ListView):
    template_name = "find-recipe.html"  
    context_object_name  = 'recipes'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['q']=self.request.GET.get('q')
        context['category_list']=Categories.objects.filter(id__in=self.request.GET.getlist('id'))
        context['category'] = Categories.objects.all()
        return context
    
    def get_queryset(self):
        query=Recipe.objects.filter(status=True)
        if self.request.GET.getlist('id'):
            query=query.filter(category__in = Categories.objects.filter(id__in=self.request.GET.getlist('id')))
        if self.request.GET.get('q'):
             query=query.filter(name__icontains=self.request.GET.get('q'))
        print(query)
        return query
    