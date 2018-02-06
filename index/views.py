#coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import View
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(requests):
    pageinfo = 1
    hl = Article.objects.filter(isPublic=True, article_type__in=(1, 2)).order_by('-pk')[0:5]
    info = Article.objects.filter(isPublic=True, article_type=1).order_by('-pk')[0:5]
    fi = Article.objects.filter(isPublic=True, article_type=2).order_by('-pk')[0:5]
    return render(requests, 'index2/index.html', locals())

def about(requests):
    pageinfo = 2
    ab = get_object_or_404(Article, title=u"关于我们")
    return render(requests, 'index2/about.html', locals())

def list(requests):
    article_type = requests.GET.get('type')
    pageinfo = 4 + int(article_type)
    article = Article.objects.filter(isPublic=True, article_type=article_type).order_by('-pk')
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
    intro = Introduce_content.objects.all()
    return render(requests, 'index2/info.html', locals())

def article(requests):
    art_id = requests.GET.get('id')
    article = get_object_or_404(Article, pk=art_id, isPublic=True)
    try:
        article_front = Article.objects.get(pk=int(art_id)-1)
    except:
        article_front = Article(title="")
    try:
        article_then = Article.objects.get(pk=int(art_id)+1)
    except:
        article_then = Article(title="")
    more_article = Article.objects.filter(isPublic=True,keyword__in=article.keyword.all()).exclude(id=article.id).order_by("-pk")
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
    intro = Fee_content.objects.all()
    return render(requests, 'index2/info.html', locals())

class Join(View):
    def get(self, requests):
        pageinfo = 3
        return render(requests, 'index2/join.html', locals())

    def post(self, requests):
        pageinfo = 3
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        aim = requests.POST.get('aim')
        others = requests.POST.get('others')
        place = requests.POST.get('place')
        Join_form(name=name, phone=phone, aim=aim, others=others, place=place).save()
        return render(requests, 'index2/join.html', locals())