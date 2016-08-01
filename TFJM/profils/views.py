from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from forms import ConnexionForm
from infos import views

def connexion(request) :
	error = False
	print ("")
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
