from __future__ import unicode_literals

from django.db import models

from profils.models import Profil

class Sujet (models.Model) :
	titre = models.CharField (max_length=30)
	id_topic = models.IntegerField (unique=True)
	
	def __unicode__ (self):
		return self.titre
	
	def save (self, *args, **kwargs):
		# surcharge de la methode save pour ajouter un id automatiquement
		if self.pk is None :
			topics = Sujet.objects.order_by ('-id_topic')
			if len(topics) == 0 :
				n_max = 0
			else :
				n_max = topics[0].id_message
			self.id_topic = n_max+1
		super (Sujet, self).save (*args, **kwargs)

class Message (models.Model):
	auteur = models.OneToOneField (Profil)
	contenu = models.TextField (blank=False)
	sujet = models.ForeignKey (Sujet)
	date_creation = models.DateTimeField (auto_now=False, auto_now_add=True)
	id_message = models.IntegerField (unique=True, blank=True)
	
	def __unicode__ (self) :
		return "message {0} dans {1}".format(self.id_message, self.sujet.titre)
	
	def save (self, *args, **kwargs):
		# surcharge de la methode save pour ajouter un id automatiquement
		if self.pk is None :
			msg = Message.objects.order_by ('-id_message')
			if len(msg) == 0 :
				n_max = 0
			else :
				n_max = msg[0].id_message
			self.id_message = n_max+1
		super (Message, self).save (*args, **kwargs)
