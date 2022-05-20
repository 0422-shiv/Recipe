from email import message
from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,db_index=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return self.name
