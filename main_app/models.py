from django.urls import reverse
from django.db import models



class Comment(models.Model):
   
    comment_field = models.TextField(max_length=500)
    #created_on = models.DateTimeField(auto_now_add=True)
    ##forigen key for linking models 
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=1, related_name='comments' )
# this wont be valid because a post doesnt exist on many comments 

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={'comment_id': self.id})
    
    def __str__(self):
        return self.comment_field
    

class Post(models.Model):
    post_field = models.TextField(max_length=500)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null = True)
    ##null true make it more secure and doesnt lalow any type of outsdie sacess 
    # created_on = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={
            'post_id': self.id,
            # 'comment_id':self.id this was uncommented beczuse it would cause an error 
            })