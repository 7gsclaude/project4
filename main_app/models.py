from django.urls import reverse
from django.db import models



class Comment(models.Model):
   
    comment_field = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={'comment_id': self.id})

class Post(models.Model):
    post_field = models.TextField(max_length=500)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    ##null true make it more secure and doesnt lalow any type of outsdie sacess 

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'post_id': self.id})
