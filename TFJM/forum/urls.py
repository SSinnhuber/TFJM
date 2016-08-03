from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^message/(?P<id_message>\d+)/$', views.message),
	url(r'^topic/(?P<id_topic>\d+)/$', views.topic),
]
