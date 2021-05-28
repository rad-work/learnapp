from django.db import models


class Subject(models.Model):
    """
    Модель отдельного предмета

    :param name: название предмета
    """
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Основная модель отдельной темы (поста)

    :param title: заголовок
    :param datetime: дата публикации, хранится в формате объекта `datetime.datetime()`
    :param content: текст поста
    :param author: автор поста
    :param subject: предмет
    """
    title = models.CharField(max_length=255, verbose_name='название')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = models.TextField(max_length=10000, verbose_name='Текст')
    author = models.CharField(max_length=255, verbose_name='Автор')
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет')

    def __unicode__(self):
        return self.title

