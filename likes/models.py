from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
class Like(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)