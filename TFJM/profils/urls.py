from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url (r'^connexion/', views.connexion, name='connexion'),
	url(r'^deconnexion/', views.deconnexion, name='deconnexion'),
	url(r'^pass_change/', auth_views.password_change, {'template_name': 'profils/pass_change.html'}),
	url(r'^password-change-done/$', auth_views.password_change_done,
    {'template_name': 'userauth/password_change_done.html'},
    name='password_change_done'),
]
	
