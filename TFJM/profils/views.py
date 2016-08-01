from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from forms import ConnexionForm
from forms import InscriptionForm

from infos import views

def connexion(request) :
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
				else:
					new_user = User(username=username, first_name=prenom, last_name=nom, email=email)
					new_user.set_password (password)
					new_user.save ()

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



