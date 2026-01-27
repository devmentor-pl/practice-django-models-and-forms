from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def recent_django_articles(request):
    articles = Article.objects.filter(title__icontains="django", published_at__gte="2024-01-01")
    for article in articles:
        print(article.title)

    Response = "<p>".join(str(article) for article in articles)
    return HttpResponse(Response)
