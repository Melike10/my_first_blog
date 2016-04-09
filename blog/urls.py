from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
] #127.0.0.1.800 den sonra blogtaki url.py den hiç bir şey gelmezse viewsin altındaki postlist metodunu çağır
