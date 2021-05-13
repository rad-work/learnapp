from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)  # заголовок поста
    datetime = models.DateTimeField(auto_now_add=True)  # дата публикации
    content = models.TextField(max_length=10000)  # текст поста
    author = models.CharField(max_length=255)  # автор

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/lesson/%i/" % self.id


'''class User(AbstractBaseUser):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    #password = models.CharField(('password'), max_length=128)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)'''