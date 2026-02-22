from django.db import models
from django.urls import reverse,reverse_lazy
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
        )
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(default=None,blank=True,null=True,upload_to='img_file/')
    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments',)
    comment = models.CharField(max_length=140)
    time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('post', args=[str(self.post_id)])

