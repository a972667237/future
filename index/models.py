#coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

ARTICLE_TYPE = (
    (0, u'页面内容'),
    (1, u'研究资讯'),
    (2, u'基础知识'),
    (3, u'业务指南')
)

AIM_TYPE = (
    (1, u'业务办理'),
    (2, u'活动报名'),
    (3, u'其他'),
    (4, u'路过，想了解一下')
)

class Key_word(models.Model):
    name = models.CharField(u"关键词", max_length=20)
    class Meta:
        verbose_name = "关键词"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    summary = models.TextField(u"摘要", max_length=10000)
    create_date = models.DateField(u'创建时间', auto_now_add=True, editable=True)
    isPublic = models.BooleanField(u'是否发布', default=True)
    article_type = models.IntegerField(u'文章类型', choices=ARTICLE_TYPE, default=1)
    author = models.CharField(u'作者', max_length=10)
    keyword = models.ManyToManyField(Key_word)
    isHithLight = models.BooleanField(u'是否为要闻', default=False)
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


class Introduce_Keyword(models.Model):
    name = models.CharField(u"关键词", max_length=20)

    class Meta:
        verbose_name = "业务信息关键词"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Fee_Keyword(models.Model):
    name = models.CharField(u"关键词", max_length=20)

    class Meta:
        verbose_name = "费率关键词"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Introduce_content(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    keyword = models.ManyToManyField(Introduce_Keyword)
    class Meta:
        verbose_name = '业务信息页面内容'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

class Fee_content(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    keyword = models.ManyToManyField(Fee_Keyword)
    class Meta:
        verbose_name = '费率页面'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

class Join_form(models.Model):
    name = models.CharField(u"姓名", max_length=100)
    aim = models.IntegerField(u"目的", choices=AIM_TYPE)
    phone = models.CharField(u"电话", max_length=11)
    place = models.CharField(u"地址", max_length=10000)
    others = models.CharField(u"其他", max_length=50000)
    isRead = models.BooleanField(u"是否已读", default=False)
    create_date = models.DateField(u"创建时间", auto_now_add=True, editable=False)
    class Meta:
        verbose_name = '加入我们提交内容'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name + "/" + self.create_date.strftime('%Y-%m-%d') + "/" + (u"已读" if self.isRead else u"未读"  )


class MainPage_article(models.Model):
    image = models.ImageField(u"图片")
    article = models.ForeignKey(Article)
    class Meta:
        verbose_name = '首页头图管理'
        verbose_name_plural = verbose_name

class JoinPage_detail(models.Model):
    topInfo = UEditorField(u'顶部信息', max_length=50000, null=True)
    bottomInfo = UEditorField(u'底部信息', max_length=50000, null=True)
    class Meta:
        verbose_name = '加入我们页面信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return u"页面信息"