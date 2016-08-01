from django.conf.urls import include, url
from . import views

urlpatterns = [
	url (r'/connexion/$', views.connexion, name='connexion'),
	url(r'/deconnexion/$', views.deconnexion, name='deconnexion'),
]
