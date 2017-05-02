from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.index),
    url(r'^message/$', views.message, name='message'),  
]