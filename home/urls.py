from django.urls import path
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name="home_view"),
    path('contact/', views.ContactUsView.as_view(), name="contact_view"),
    path('recipe-upload/', views.UploadRecipeView.as_view(), name="upload_recipe_view")

]