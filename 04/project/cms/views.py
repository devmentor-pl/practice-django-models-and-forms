from cms.models import Article
from django.http import HttpResponse


def recent_django_articles(request):

    articles = Article.objects.filter(title__icontains="django", published_at__gte="2024-01-01")

    titles = []

    for article in articles:
        titles.append(article.title)

    return HttpResponse("\n".join(titles), content_type="text/plain; charset=utf-8")
