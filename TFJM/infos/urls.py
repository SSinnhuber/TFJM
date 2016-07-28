from django.conf.urls import include, url
from . import views

urlpatterns = [
	url (r'^$', views.accueil),
	url(r'^portail/(?P<nom_portail>[a-zA-Z0-9_-]+)$', views.portail),
	url(r'^article/(?P<nom_article>[a-zA-Z0-9_-]+)$', views.article),
]
	
