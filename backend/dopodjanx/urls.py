from django.conf.urls import url
from dopodjanx import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^companies/$', views.companiesApi)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
