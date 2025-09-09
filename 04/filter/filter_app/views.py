from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Article
from datetime import date


def recent_django_articles(request):
    django_articles = Article.objects.filter(
        title__contains='Django', published_at__gt=(date(2024, 1, 1)))
    article_list = [article.title for article in django_articles]
    article = "\n".join(article_list)

    return HttpResponse(article, content_type="text/plain")


# Create your views here.
