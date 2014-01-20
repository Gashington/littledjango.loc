# -*- coding: utf-8 -*-

from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField

# Create your models here.

class Alias(models.Model):
    title = models.CharField(u'Название',max_length=100)
    alias = models.SlugField(max_length=100, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = translit.slugify(self.title)
        super(Alias, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(Alias):
    pass

    class Meta:
        verbose_name_plural = u"Категории"


class Tag(Alias):
    pass

    class Meta:
        verbose_name_plural = u"Метки"


class Post(Alias):

    content = RichTextField(u'Контент')
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    tags = models.ManyToManyField(Tag, verbose_name=u'Метки')

    class Meta:
        verbose_name_plural = u"Записи"


