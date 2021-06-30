from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
class Post_Kids(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='kids_posts')
    img= models.ImageField(upload_to='admin/%Y/%m/%d/',
                            blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    visits  = models.PositiveIntegerField(default=0)
    summary = models.TextField(default='', max_length=500)
    tags = TaggableManager()
    class Meta:
      ordering = ('-publish',)
    def __str__(self):
          return self.title
    def get_absolute_url(self):
          return reverse('ListKids:post_kids_detail',
                        args=[self.publish.year,
                        self.publish.month,
                        self.publish.day, self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post_Kids,
    on_delete=models.CASCADE,
    related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
      ordering = ('created',)
    def __str__(self):
     return 'Comment by +{self.name}+ on +{self.post}'