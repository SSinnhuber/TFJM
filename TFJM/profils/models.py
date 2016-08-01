from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profil (models.Model):
	user = models.OneToOneField (User)
	bio = models.TextField (blank=True)
	
	def __str__ (self) :
		return self.user.username
