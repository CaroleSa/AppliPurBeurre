from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^result/$', views.result),
    url(r'^detail/$', views.detail),
    url(r'^favorites/$', views.favorites)
]
