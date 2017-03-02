from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^friend/(?P<id>\d+)$', views.friend),
    url(r'^unfriend/(?P<id>\d+)$', views.unfriend),
    url(r'^delete_user/(?P<id>\d+)$', views.delete_user),
]
