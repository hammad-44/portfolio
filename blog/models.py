
# Create your models here.
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    dispic=models.TextField(default=0)
    views= models.IntegerField(default=0)
    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    name=models.CharField(max_length=130, default="")
    email=models.CharField(max_length=130, default="")
    comment=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    