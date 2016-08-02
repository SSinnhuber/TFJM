from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.db.models.signals import post_save
import os

class Profil (models.Model):
	user = models.OneToOneField (User)
	img = models.ImageField (upload_to="profil", blank=True)
	bio = models.TextField (blank=True)
	id_user = models.IntegerField (unique=True)
	
	def __str__ (self) :
		return self.user.username

	def save (self, *args, **kwargs):
		
		if self.pk is None :
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

