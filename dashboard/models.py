from distutils.command.upload import upload
from django.db import models
from user.models import User
# Create your models here.

class Categories(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Recipe(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='recipe_photos',verbose_name="recipe photo")
    video=models.FileField(upload_to="videos" )
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    description = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
