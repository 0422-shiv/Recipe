from django.urls import path
from . import views

urlpatterns = [

    path('', views.MyProfileView.as_view(), name="my_profile_view"),
    path('change-password', views.ChangePasswordView.as_view(), name="change_password_view"),
    path('upload', views.RecipeUploadView.as_view(), name="recipe_upload_view"),
     path('my-recipe', views.MyRecipeView.as_view(), name="my_recipe_view"),

]