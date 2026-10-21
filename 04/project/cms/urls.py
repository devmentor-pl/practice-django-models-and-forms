from django.urls import path
from cms.views import recent_django_articles


urlpatterns = [
    path("django-recent/", recent_django_articles, name="django-recent")
]
