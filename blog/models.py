from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model to define the fields required to create a single blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    """Model to define the fields required to create the Comments under a
    blog post"""
    comment_detail = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_detail
