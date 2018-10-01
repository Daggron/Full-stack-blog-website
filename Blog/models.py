from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    post_title = models.CharField(max_length=1000)
    post_about = models.CharField(max_length=2000)
    post_description = models.CharField(max_length=1000)
    post_body = models.TextField()
    post_photo = models.FileField(default=None)
    published_date = models.DateTimeField(null=True , blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.post_title
