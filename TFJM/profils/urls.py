from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

# il est nécessaire de recoder les templates des gestion d'User sans quoi django appelle les templates par défaut
# qui n'utilisent pas les même fichiers de style que le reste du site

# ! pb de l'envoi de mail à régler
urlpatterns = [
	url(r'^', include('django.contrib.auth.urls')),
	url (r'^connexion/', views.connexion, name='connexion'),
	url(r'^deconnexion/', views.deconnexion, name='deconnexion'),
	url(r'^pass_change/', auth_views.password_change, {'template_name': 'profils/pass_change.html'}),
	url(r'^password_change_done/$', auth_views.password_change_done,
		{'template_name': 'profils/password_change_done.html'},
		name='password_change_done'),
	url(r'^pass_reset/', auth_views.password_reset, {'template_name': 'profils/pass_reset.html'}),
	url(r'^password_reset_done/$', auth_views.password_reset_done,
		{'template_name': 'profils/password_reset_done.html'},
		name='password_reset_done'),
	url(r'^password_reset_confirm/$', auth_views.password_reset_confirm,
		{'template_name': 'profils/password_reset_confirm.html'}),
	url(r'^password_reset_done/$', auth_views.password_reset_done,
		{'template_name': 'profils/password_reset_done.html'},
		name='password_reset_done'),
	url(r'^password_reset_complete/$', auth_views.password_reset_complete,
		{'template_name': 'profils/password_reset_complete.html'},
		name='password_reset_complete'),
	url (r'^inscription/$', views.inscription),
	url(r'^user/(?P<id_user>\d+)/$', views.user),
	url(r'^me/$', views.me),
	url(r'^maj-profil/$', views.maj_profil),
]
	
