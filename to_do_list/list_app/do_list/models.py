from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class name_list(models.Model):
    username = models.CharField(max_length = 50)     

    def __str__(self) -> str:
        return f"{self.username}"
    
class to_do_list(models.Model):
    
    user_list = models.CharField(max_length = 50)
    user_names_list = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
    
    def __str__(self) -> str:
        return f"{self.user_list}"    

