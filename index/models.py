#coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

ARTICLE_TYPE = (
    (0, u'页面内容'),
    (1, u'研究资讯'),
    (2, u'金融知识')
)

class Article(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    create_date = models.DateField(u'创建时间', auto_now_add=True, editable=True)
    isPublic = models.BooleanField(u'是否发布', default=True)
    article_type = models.IntegerField(u'文章类型', choices=ARTICLE_TYPE, default=1)
    author = models.CharField(u'作者', max_length=10)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

class ContactInfo(models.Model):
    name = models.CharField(u'联系人', max_length=10)
    photo = models.CharField(u'电话', max_length=11)
    qq = models.CharField(u'QQ', max_length=11)
    mail = models.EmailField(u'邮箱')

    class Meta:
        verbose_name = '联系人信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Introduce_content(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    class Meta:
        verbose_name = '介绍页面'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

class Fee_content(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    class Meta:
        verbose_name = '收费页面'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title