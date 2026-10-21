from django.urls import path
from cms.views import contact_view


urlpatterns = [
    path("contact/", contact_view, name="contact")
]
