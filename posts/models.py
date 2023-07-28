from django.db import models
from django.conf import settings

class Post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.ForeignKey('buildings.Location', on_delete=models.CASCADE)
    purpose = models.ForeignKey('buildings.Purpose', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f'Post by {self.writer} named {self.title}'
    
class Comment(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    original_post = models.ForeignKey(Post, one_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.writer} on post {self.original_post}'