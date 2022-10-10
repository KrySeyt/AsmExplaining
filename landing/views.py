from django.http import HttpRequest
from django.shortcuts import render
from django.db.models import QuerySet

from .models import Article


def _show_article(request: HttpRequest, article: Article, context: dict = None):

    context = context or dict()
    context['article'] = article

    return render(request, 'landing/article.html', context)


def show_article(request: HttpRequest, article_pk: int):
    article: QuerySet = Article.objects.get(pk=article_pk)

    return show_article(request, article)


def main(request: HttpRequest):
    article: QuerySet = Article.objects.get(is_main=True)

    return _show_article(request, article)
