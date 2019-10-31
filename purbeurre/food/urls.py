from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    url(r'^result/$', views.result,  name="result"),
    path('detail/<name>', views.detail, name="detail"),
    url(r'^favorites/$', views.favorites, name="favorites")
]
