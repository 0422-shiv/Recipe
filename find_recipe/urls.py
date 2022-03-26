from django.urls import path
from . import views

urlpatterns = [

    path('', views.FindRecipeView.as_view(), name="find_recipe_view")

]