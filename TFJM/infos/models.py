# coding: utf-8


from __future__ import unicode_literals
from django.db import models


# la classe Categorie correspond aux parties du menu principal
class Categorie (models.Model) :
	nom = models.CharField (max_length=30)
	slug = models.SlugField (max_length=30, unique=True) # sert a identifier la categorie dans l'url
	description = models.TextField (null=True)
	image = models.ImageField (upload_to='photos/')
	def __unicode__ (self) :
		return self.nom

# la classe Sscategorie correspond aux sous-blocs des portails
class Sscategorie (models.Model) :
	nom = models.CharField (max_length=30)
	cat = models.ForeignKey ('Categorie')
	image = models.ImageField (upload_to='photos/')
	def __unicode__ (self) :
		return self.nom

# Une sous categorie peut contenir un lien interne vers un article ou un lien externe
class Lien (models.Model) :
	titre = models.CharField (max_length=100)
	adresse = models.FileField (upload_to='files/', null=True,blank=True)
	lienhttp = models.CharField (max_length=100, null=True,blank=True)
	isLienhttp = models.BooleanField ()
	sscat = models.ForeignKey ('Sscategorie')

	def __unicode__ (self):
		return self.titre

# la classe Article definit une page
class Article (models.Model)  :
	titre = models.CharField (max_length=100)
	slug = models.SlugField (max_length=100, unique=True)
	sscat = models.ForeignKey ('Sscategorie')
	date = models.DateTimeField (auto_now_add=True, auto_now=False, verbose_name="Date de creation")
	contenu = models.TextField (null=True)

	def __unicode__ (self) :
		return self.titre
