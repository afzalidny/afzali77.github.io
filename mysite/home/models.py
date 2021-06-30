from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Main(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    auther = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Main_posts')
    img= models.CharField(default='', max_length=1500)
    
   
   