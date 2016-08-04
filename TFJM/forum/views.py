from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from profils.models import Profil
from models import Message, Sujet
from forms import ReponseForm, SujetForm

def message (request, id_message):
	msg = get_object_or_404 (Message, id_message=id_message)
	print (msg)
	return render(request, 'forum/message.html', locals())

def topic (request, id_topic):
	sujet = get_object_or_404 (Sujet, id_topic=id_topic)
	messages = Message.objects.filter (sujet=sujet)#.order_by ('date_creation')
	admin = False
	if request.user.is_authenticated () and request.user.is_staff :
		admin = True
	return render (request, 'forum/topic.html', locals ())

def forum (request):
	sujets = Sujet.objects.all ().order_by ('date_dernier_message')
	n_message = []
	for sj in sujets :
		n = len (Message.objects.filter (sujet=sj) )
		n_message.append ( n )
	liste = zip (sujets, n_message)
	return render (request, 'forum/forum.html', locals ())

@login_required
def reponse (request, id_topic):
	sujet = get_object_or_404 (Sujet, id_topic=id_topic)
	if request.method == 'POST':
		form = ReponseForm(request.POST)
		if form.is_valid():
			message = Message ()
			pr = get_object_or_404 (Profil, user=request.user)
			message.auteur = pr
			message.contenu = form.cleaned_data ['reponse']
			message.sujet = sujet
			message.save()
			return redirect (topic, id_topic)
		else :
			error = True
	else:
		form = ReponseForm()
	return render(request, 'forum/reponse.html', locals())

@login_required
def suppr_message (request, id_message):
	if request.user.is_staff :
		msg = get_object_or_404 (Message, id_message=id_message)
		sj = msg.sujet
		messages = Message.objects.filter (sujet=sj).order_by('date_creation')
		if msg != messages[0] :
			msg.delete ()
		return redirect (topic, sj.id_topic)

@login_required
def nouveau_sujet (request) :
	if request.method == 'POST':
		form = SujetForm(request.POST)
		if form.is_valid():
			sujet = Sujet ()
			sujet.titre = form.cleaned_data ['titre']
			pr_createur = get_object_or_404 (Profil, user=request.user)
			sujet.createur = pr_createur
			sujet.save ()
			message = Message ()
			message.auteur = pr_createur
			message.contenu = form.cleaned_data ['message']
			message.sujet = sujet
			message.save()
			return redirect (topic, sujet.id_topic)
		else :
			error = True
	else:
		form = SujetForm()
	return render(request, 'forum/nouveau.html', locals())
	
	
