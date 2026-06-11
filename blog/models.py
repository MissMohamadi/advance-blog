from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    '''
    This is s class to define posts for blog app.
    '''
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Category(models.Model):
    '''
    This is a class to define category of posts in blog app.
    '''
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name