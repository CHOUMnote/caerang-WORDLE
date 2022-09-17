from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)