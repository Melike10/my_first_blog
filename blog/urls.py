from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
] #127.0.0.1.800 den sonra blogtaki url.py den hiç bir şey gelmezse viewsin altındaki postlist metodunu çağır
