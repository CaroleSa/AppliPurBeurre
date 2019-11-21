from django.conf.urls import url
from . import views


app_name = 'food'

urlpatterns = [
    url(r'^result/$', views.result,  name="result"),
    url(r'^detail/$', views.detail, name="detail"),
    url(r'^favorites/$', views.favorites, name="favorites"),
    url(r'^mentions_legal/$', views.mentions_legal, name="mentions_legal")
]
