
from django.urls import reverse

# Create your models here.
from django.db import models
        

class Post (models.Model):
    post_field = models.TextField(max_length=500)
    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'post_id': self.id})
    
# class Comment (models.Model):
#     post_field = models.TextField(max_length=500)
    