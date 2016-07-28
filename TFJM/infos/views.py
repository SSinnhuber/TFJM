# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models

def accueil (request) :
	return render (request, 'infos/accueil.html', {})

def portail (request, nom_portail):
	categorie = get_object_or_404(models.Categorie, slug=nom_portail)
	sscategories = models.Sscategorie.objects.filter (cat=categorie)
	liens = []
	articles = []
	nb=0
	for sc in sscategories :
		articles.append( models.Article.objects.filter(sscat = sc) )
		liens.append ( models.Lien.objects.filter (sscat = sc) )
	listes = zip (sscategories, articles, liens)
	return render (request, 'infos/portail.html', locals())

def article (request, nom_article):
	article = get_object_or_404 (models.Article, slug=nom_article)
	return render (request, 'infos/article.html', {'article' : article})
	
