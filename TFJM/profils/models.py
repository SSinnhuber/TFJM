from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.db.models.signals import post_save
import os


#Un profil correspond a un utilisateur
#En plus des attributs de la classe User, on rajoute d'autres variables correspondant a l'idee que l'on a d'un profil
# ces differentes informations sont (selon les autorisations) visibles dans la page profil de l'utilisateur (cf. views.py)
# ! les superutilisateurs aussi ont une instance de Profil associé
class Profil (models.Model):
	user = models.OneToOneField (User)
	img = models.ImageField (upload_to="profil", blank=True) # avatar du profil
	bio = models.TextField (blank=True) # description
	id_user = models.IntegerField (unique=True) # l'identifiant de l'utilisateur sert à coder l'url pour sa page profil
	
	def __str__ (self) :
		return self.user.username

	def save (self, *args, **kwargs):
# pour que l'utilisateur n'ait pas a creer lui meme son identifiant, celui-ci est cree automatiquement lors de la sauvegarde dans la BDD
# ! lors de la creation d'un (super)utilisateur depuis les pages admin, ne PAS remplir le champ id_user (risque de collision)
		if self.pk is None :
			# cette condition permet de tester s'il s'agit de la première sauvegarde de l'objet
			profils = Profil.objects.order_by ('-id_user')
			if len(profils) == 0 :
				n_max = 0
			else :
				n_max = profils[0].id_user
			self.id_user = n_max+1
		super (Profil, self).save (*args, **kwargs)


def create_profil (sender, instance, **kwargs):
	if len (Profil.objects.filter (user=instance) ) == 0 :
		pr = Profil (user=instance)
		pr.save ()

post_save.connect(create_profil, sender=User)
# permet de creer un profil si une instance de User est creee depuis les pages admin
