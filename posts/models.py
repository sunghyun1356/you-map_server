from django.db import models
from django.conf import settings
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    location = models.ForeignKey('buildings.Location', related_name='posts', on_delete=models.CASCADE)
    purpose = models.ForeignKey('buildings.Purpose', related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/', blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'Post by {self.writer} named {self.title}'
    
class Comment(TimeStampedModel):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    original_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.writer} on post {self.original_post}'