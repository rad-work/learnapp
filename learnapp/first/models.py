from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(auto_now_add=True) # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/lesson/%i/" % self.id