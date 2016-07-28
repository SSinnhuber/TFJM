from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models

def accueil (request) :
	return render (request, 'infos/accueil.html', {})

def portail (request, nom_portail):
	categorie = get_object_or_404(models.Categorie, slug=nom_portail)
	articles = models.Article.objects.filter(sscat__cat = categorie)
	liens = models.Lien.objects.filter (sscat__cat = categorie)
	return render (request, 'infos/portail.html', locals())

def article (request, nom_article):
	article = get_object_or_404 (models.Article, slug=nom_article)
	return render (request, 'infos/article.html', {'article' : article})
	
