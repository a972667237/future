#coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(requests):
    hl = Article.objects.filter(isPublic=True, article_type__in=(1, 2)).order_by('-pk')[0:5]
    info = Article.objects.filter(isPublic=True, article_type=1).order_by('-pk')[0:2]
    fi = Article.objects.filter(isPublic=True, article_type=2).order_by('-pk')[0:2]
    contact_info = ContactInfo.objects.get(id=1)
    return render(requests, 'index/index.html', locals())

def about(requests):
    hl = Article.objects.filter(isPublic=True, article_type__in=(1, 2)).order_by('-pk')[0:5]
    ab = get_object_or_404(Article, title=u"关于我们")
    contact_info = ContactInfo.objects.get(id=1)
    return render(requests, 'index/about.html', locals())

def list(requests):
    article_type = requests.GET.get('type')
    hl = Article.objects.filter(isPublic=True, article_type__in=(1, 2)).order_by('-pk')[0:5]
    contact_info = ContactInfo.objects.get(id=1)
    article = Article.objects.filter(isPublic=True, article_type=article_type).order_by('-pk')
    art_len = article.count()
    paginator = Paginator(article, 3)
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
    if end + art_index > art_len/3 + 1:
        end = int(art_len/3 + 1 - art_index)
    page_list = range(art_index-front, art_index+end+1)
    return render(requests, 'index/article_list.html', locals())

def introduce(requests):
    hl = Article.objects.filter(isPublic=True, article_type__in=(1, 2)).order_by('-pk')[0:5]
    contact_info = ContactInfo.objects.get(id=1)
    future_account = get_object_or_404(Article, title=u"期货开户")
    option_account = get_object_or_404(Article, title=u'期权开户')
    intermediary_recruitment = get_object_or_404(Article, title=u'居间招募')
    return render(requests, 'index/introduce.html', locals())

def article(requests):
    art_id = requests.GET.get('id')
    article = get_object_or_404(Article, pk=art_id, isPublic=True)
    return render(requests, 'index/article.html', locals())