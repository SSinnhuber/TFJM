from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^message/(?P<id_message>\d+)/$', views.message),
	url(r'^topic/(?P<id_topic>\d+)/$', views.topic),
	url(r'^$', views.forum),
	url(r'^reponse/(?P<id_topic>\d+)/$', views.reponse),
	url(r'^suppr-message/(?P<id_message>\d+)/$', views.suppr_message),
	url(r'^nouveau-sujet/$', views.nouveau_sujet),
]
