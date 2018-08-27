from django.db import models
from django.contrib.auth.models import AbstractBaseUser as BaseUser, AbstractUser
from django.db.models import CASCADE
from django.conf import settings

class User(AbstractUser):
    is_Admin = models.BooleanField(blank=True, null=True)

class Tag(models.Model):
    tag_name=models.CharField(max_length=50,unique=True)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    tag_name = models.ForeignKey(Tag, on_delete=CASCADE)
    description = models.CharField(max_length=100)
    time = models.TimeField()

class Comments(models.Model):
    class Meta:
        verbose_name_plural = 'comments'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    article = models.ForeignKey(Article, on_delete=CASCADE)
    description = models.CharField(max_length=100)
    time = models.TimeField()


    # Create your models here.
