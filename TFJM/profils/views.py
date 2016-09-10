from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile

from PIL import Image

from forms import ConnexionForm
from forms import InscriptionForm
from forms import ProfilForm

from models import Profil

# Profil est une classe derivee de User, cf. models.py pour les attributs

from infos import views

def connexion(request) :
# cette fonction utilise le systeme d'User de django
	error = False
	if request.method == 'POST':	
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password) 
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect (views.accueil)
					# apres connexion l'utilisateur est redirige sur la page d'accueil
				else:
					error = True
			else:
				error = True
	else:
		form = ConnexionForm()
	return render(request, 'profils/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(views.accueil)


def inscription (request) :
# formulaire de creation de profil
# le formulaire ne cree qu'une instance de User, le signal cree par la suite l'instance de Profil (cf. models.py)
	error = False
	diff = False
	already_exist = False
	if request.method == 'POST':
		form = InscriptionForm(request.POST)
		if form.is_valid():
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			prenom = form.cleaned_data['prenom']
			nom = form.cleaned_data['nom']
			email = form.cleaned_data['email']
			if password != confirm_password :
				diff = True
			else:
				if len (User.objects.filter (username=username))>0 :
					already_exist = True
					# permet d'afficher une erreur si le pseudonyme entre est deja utilise
				else:
					new_user = User(username=username, first_name=prenom, last_name=nom, email=email)
					new_user.set_password (password)
					new_user.save ()
					#les donnees sont valides, on cree l'utilisateur et on le connecte
					user = authenticate(username=username, password=password)
					if user is not None:
						if user.is_active:
							login(request, user)
						else:
							error = True
					else:
						error = True
	else:
		form = InscriptionForm()
		new_user = None
	return render(request, 'profils/inscription.html', locals())

@login_required
def user (request, id_user) :
	# page du profil. Non accessible aux utilisateurs non connectes, affiche certaines des informations du profil,
	# selon si l'utilisateur a les droits admin ou non. cf. le template profils/profil.html pour le detail
	profil = get_object_or_404 (Profil, id_user=id_user)
	return render(request, 'profils/profil.html', locals())

@login_required
def me (request) :
	# page du profil de l'utilisateur. Idem que ci-dessus
	profil = get_object_or_404 (Profil, user=request.user)
	print (profil.img)
	return render(request, 'profils/profil.html', locals())

# permet de creer une miniature de l'avatar de l'utilisateur
def create_thumbnail (img_url) :
	size = (240,240)
	
	im = Image.open (img_url)
	im.thumbnail (size)
	im.save (img_url, "JPEG")	
	
@login_required
# modification des infos du profil
def maj_profil(request):
	error = False
	profil = get_object_or_404 (Profil, user=request.user)
	if request.method == 'POST':
		form = ProfilForm(request.POST, request.FILES)
		if form.is_valid():
			profil.user.first_name = form.cleaned_data['prenom']
			profil.user.last_name = form.cleaned_data['nom']
			profil.user.email = form.cleaned_data['email']
			profil.bio = form.cleaned_data['bio']
			# le if est necessaire pour ne pas supprimer l'ancien avatar dans le cas ou l'utilisateur n'en upload pas un nouveau
			if not (form.cleaned_data['img'] is None) :
				profil.img = form.cleaned_data['img']
			profil.user.save()
			profil.save()
			return redirect (me)
		else :
			error = True
	else:
		data = {'prenom': profil.user.first_name,
				'nom': profil.user.last_name,
				'email': profil.user.email,
				'bio': profil.bio,
				}
	#	file_data = {'img': SimpleUploadedFile(profil.img.url, profil.img.read())}
		form = ProfilForm(data)
	return render(request, 'profils/maj_profil.html', locals())
