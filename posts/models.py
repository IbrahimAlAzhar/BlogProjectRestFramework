from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)  # here author is fk of User
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # this attribute added automatically
    updated_at = models.DateTimeField(auto_now=True) # when we update a post,automatically take this

    def __str__(self): # this is the string representation of Post class show in admin and others
        return self.title
