from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from profils.models import Profil
from models import Message, Sujet
from forms import ReponseForm, SujetForm

# cf. profils/models.py et forum/models.py pour les implementations de Sujet, Message et Profil

# page d'affichage du message. Cf le template pour plus de details
def message (request, id_message):
	msg = get_object_or_404 (Message, id_message=id_message)
	print (msg)
	return render(request, 'forum/message.html', locals())

# page des messages du sujet. 
def topic (request, id_topic):
	sujet = get_object_or_404 (Sujet, id_topic=id_topic)
	messages = Message.objects.filter (sujet=sujet)#.order_by ('date_creation')
	# Il est important d'afficher les messages dans l'ordre chronologique
	admin = False
	if request.user.is_authenticated () and request.user.is_staff :
		admin = True
		# si l'utilisateur est admin, il peut supprimer directement les messages au cas par cas
		# Cf. le template + la fonction suppr_message
	return render (request, 'forum/topic.html', locals ())

# la liste des sujets du forum
def forum (request):
	sujets = Sujet.objects.all ().order_by ('-date_dernier_message')
	n_message = []
	for sj in sujets :
		n = len (Message.objects.filter (sujet=sj) )
		n_message.append ( n )
	liste = zip (sujets, n_message)
	# cette methode permet d'afficher le nombre de message du sujet sans avoir a ajouter un nouvel attribut
	admin=False
	if request.user.is_authenticated () and request.user.is_staff :
		admin = True
		# un admin dispose d'un lien supplementaire pour supprimer un sujet
	return render (request, 'forum/forum.html', locals ())

@login_required
def reponse (request, id_topic):
#  Si l'utilisateur est connecte, il peut repondre au sujet
	sujet = get_object_or_404 (Sujet, id_topic=id_topic)
	if request.method == 'POST':
		form = ReponseForm(request.POST)
		if form.is_valid():
			message = Message ()
			pr = get_object_or_404 (Profil, user=request.user)
			#profil associe a l'utilisateur connecte
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
# un admin peut supprimer un message (sauf le premier). Il est redirige dans la foulee sur la page associee au sujet
	if request.user.is_staff :
		msg = get_object_or_404 (Message, id_message=id_message)
		sj = msg.sujet
		messages = Message.objects.filter (sujet=sj).order_by('date_creation')
		if msg != messages[0] :
			msg.delete ()
			# on prend cette précaution pour eviter le bypass via l'url, meme si il n'y a pas le lien sur la page
		return redirect (topic, sj.id_topic)

@login_required
def nouveau_sujet (request) :
# permet a un utilisateur de creer un nouveau sujet
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
	
@login_required
def suppr_sujet (request, id_topic):
# un admin peut supprimer un sujet
	if request.user.is_staff :
		sj = get_object_or_404 (Sujet, id_topic=id_topic)
		sj.delete ()
		return redirect (forum)
