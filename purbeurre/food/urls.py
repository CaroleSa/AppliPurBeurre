from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^result/$', views.result,  name="result"),
    url(r'^detail/$', views.detail, name="detail"),
    url(r'^favorites/$', views.favorites, name="favorites")
]
