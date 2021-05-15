from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')  # заголовок поста
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')  # дата публикации
    content = models.TextField(max_length=10000, verbose_name='Текст')  # текст поста
    author = models.CharField(max_length=255, verbose_name='Автор')  # автор
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет')

    def __unicode__(self):
        return self.title

