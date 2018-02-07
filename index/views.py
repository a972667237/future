#coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import View
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(requests):
    pageinfo = 1
    hl = Article.objects.filter(isPublic=True, article_type__in=(1, 2), isHithLight=True).order_by('-pk')[0:5]
    info = Article.objects.filter(isPublic=True, article_type=1).order_by('-pk')[0:5]
    fi = Article.objects.filter(isPublic=True, article_type=2).order_by('-pk')[0:5]
    po = Article.objects.filter(isPublic=True, article_type=3).order_by('-pk')[0:5]
    head = MainPage_article.objects.all()
    return render(requests, 'index2/index.html', locals())

def about(requests):
    pageinfo = 2
    ab = get_object_or_404(Article, title=u"关于我们")
    return render(requests, 'index2/about.html', locals())

def list(requests):
    article_type = int(requests.GET.get('type', 1))
    keyword = int(requests.GET.get('keyword', 0))
    hot_key = Key_word.objects.all()[0:6]
    pageinfo = 4 + article_type
    if keyword == 0:
        article = Article.objects.filter(isPublic=True, article_type=article_type).order_by('-pk')
    else:
        k = Key_word.objects.filter(id=keyword)
        article = Article.objects.filter(isPublic=True, article_type=article_type, keyword=k)
    art_len = article.count()
    paginator = Paginator(article, 5)
    try:
        page = int(requests.GET.get('page', 1))
        article = paginator.page(page)
    except(EmptyPage, InvalidPage):
        article = paginator.page(1)
        page = 1
    art_index = page
    front = art_index - 1
    if front > 2:
        front = 2
    end = 4 - front
    if end + art_index > art_len/5 + 1:
        end = int(art_len/5 + 1 - art_index)
    page_list = range(art_index-front, art_index+end+1)
    return render(requests, 'index2/article_list.html', locals())

def introduce(requests):
    pageinfo = 4
    keyword = int(requests.GET.get('keyword', 0))
    hot_key = Introduce_Keyword.objects.all()
    if keyword == 0:
        intro = Introduce_content.objects.all()
    else:
        k = Introduce_Keyword.objects.get(id=keyword)
        intro = Introduce_content.objects.filter(keyword=k)
    return render(requests, 'index2/info.html', locals())

def article(requests):
    art_id = requests.GET.get('id')
    article = get_object_or_404(Article, pk=art_id, isPublic=True)
    pageinfo = 4 + article.article_type
    try:
        article_front = Article.objects.exclude(article_type=0).exclude(article_type=3).get(pk=int(art_id)-1)
    except:
        article_front = Article(title="")
    try:
        article_then = Article.objects.exclude(article_type=0).exclude(article_type=3).get(pk=int(art_id)+1)
    except:
        article_then = Article(title="")
    more_article = Article.objects.filter(isPublic=True,keyword__in=article.keyword.all()).exclude(id=article.id).exclude(article_type=0).exclude(article_type=3).order_by("-pk")
    more_article_temp = []
    for i in more_article:
        canSave = True
        for j in more_article_temp:
            if i.id == j.id:
                canSave = False
                break
        if canSave:
            more_article_temp.append(i)
            if len(more_article) == 5:
                break
    more_article = more_article_temp
    return render(requests, 'index2/article.html', locals())

def fee(requests):
    pageinfo = 7
    keyword = int(requests.GET.get('keyword', 0))
    hot_key = Fee_Keyword.objects.all()
    if keyword == 0:
        intro = Fee_content.objects.all()
    else:
        k = Fee_Keyword.objects.get(id=keyword)
        intro = Fee_content.objects.filter(keyword=k)
    return render(requests, 'index2/info.html', locals())

class Join(View):
    def get(self, requests):
        pageinfo = 3
        po = Article.objects.filter(isPublic=True, article_type=3).order_by('-pk')[0:5]
        jo = JoinPage_detail.objects.get(id=1)
        return render(requests, 'index2/join.html', locals())

    def post(self, requests):
        import re
        name = requests.POST.get('name')
        if len(name) == 0:
            return HttpResponse("必须输入名字")
        phone = requests.POST.get('phone')
        p = re.compile('^0\d{2,3}\d{7,8}$|^1[3578]\d{9}$|^147\d{8}')
        if not p.match(phone):
            return HttpResponse("手机格式有误")
        aim = requests.POST.get('aim')
        if not aim:
            return HttpResponse("必须选择一个目的")
        others = requests.POST.get('others')
        place = requests.POST.get('place')
        try:
            Join_form(name=name, phone=phone, aim=aim, others=others, place=place).save()
        except:
            return HttpResponse("不可预知的错误")
        return HttpResponse("提交成功")

def search(requests):
    pageinfo = 8
    kv = requests.GET.get('keyword', u'移动')
    article = Article.objects.filter(isPublic=True, keyword__name__contains=kv, article_type__in=(1, 2))
    art_len = article.count()
    paginator = Paginator(article, 5)
    try:
        page = int(requests.GET.get('page', 1))
        article = paginator.page(page)
    except(EmptyPage, InvalidPage):
        article = paginator.page(1)
        page = 1
    art_index = page
    front = art_index - 1
    if front > 2:
        front = 2
    end = 4 - front
    if end + art_index > art_len / 5 + 1:
        end = int(art_len / 5 + 1 - art_index)
    page_list = range(art_index - front, art_index + end + 1)
    return render(requests, 'index2/article_list.html', locals())
