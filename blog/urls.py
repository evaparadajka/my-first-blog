from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^klient_list', views.klient_list, name='klient_list'),
    url(r'^klient/new/$', views.klient_new, name='klient_new'),
    url(r'^klient/(?P<numerkarty>[0-9]+)/$', views.klient_detail, name='klient_detail'),
    url(r'^klient/(?P<numerkarty>[0-9]+)/edit/$', views.klient_edit, name='klient_edit'),
    url(r'^klient/(?P<numerkarty>[0-9]+)/odlicz/$', views.klient_odlicz, name='klient_odlicz'),
]
