from __future__ import unicode_literals

from django.db import models

from profils.models import Profil
from datetime import datetime    

# le forum est mis en place sous la forme d'une premiere page regroupant la liste des sujets deja ecrits,
# qui redirige vers la liste des messages publies sur chaque sujet

# chaque message contient un encadre avec le nom de son auteur, et un lien redirigeant vers son profil

# sujet regroupe un ensemble de message
# ! de meme que pour profil, ne PAS modifier a la main id_topic depuis les pages d'admin
class Sujet (models.Model) :
	titre = models.CharField (max_length=30)
	id_topic = models.IntegerField (unique=True, blank=True)
	# de meme que pour Profil, id_sujet sert a identifier l'url d'acces aux messages du sujet
	date_dernier_message = models.DateTimeField (default=datetime.now, blank=True)
	# ce champ doit etre mis a jour a chaque enregistrement d'un nouveau message dans le sujet, cf. plus bas
	
	createur = models.ForeignKey (Profil)
	def __unicode__ (self):
		return self.titre
	
	def save (self, *args, **kwargs):
		# surcharge de la methode save pour ajouter un id automatiquement
		if self.pk is None :
			topics = Sujet.objects.order_by ('-id_topic')
			# lors de l'enregistrement on ajoute le nouveau sujet a la liste topics (triee par ordre chronologique)
			if len(topics) == 0 :
				n_max = 0
			else :
				n_max = topics[0].id_topic
			# n_max est l'id du dernier topic, et permet d'assigner au sujet son id lors de l'enregistrement
			self.id_topic = n_max+1
		super (Sujet, self).save (*args, **kwargs)





class Message (models.Model):
	auteur = models.ForeignKey (Profil)
	contenu = models.TextField (blank=False)
	sujet = models.ForeignKey (Sujet)
	date_creation = models.DateTimeField (auto_now=False, auto_now_add=True)
	id_message = models.IntegerField (unique=True, blank=True)
	
	def __unicode__ (self) :
		return "message {0} dans {1}".format(self.id_message, self.sujet.titre)
	
	def save (self, *args, **kwargs):
		# surcharge de la methode save pour ajouter un id automatiquement, et modifier les proprietes du sujet associe
		if self.pk is None :
			msg = Message.objects.order_by ('-id_message')
			if len(msg) == 0 :
				n_max = 0
			else :
				n_max = msg[0].id_message
			self.id_message = n_max+1 # meme principe que pour Sujet
			self.sujet.date_dernier_message = self.date_creation
		super (Message, self).save (*args, **kwargs)
