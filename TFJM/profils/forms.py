from django import forms
from models import Profil

class ConnexionForm (forms.Form):
	username = forms.CharField (label="Nom d'utilisateur", max_length=30)
	password = forms.CharField (label="Mot de passe", widget=forms.PasswordInput)

class InscriptionForm (forms.Form):
	username = forms.CharField (label="Nom d'utilisateur", max_length=30)
	password = forms.CharField (label="Mot de passe", widget=forms.PasswordInput)
	confirm_password = forms.CharField (label="Confirmez le mot de passe", widget=forms.PasswordInput)
	prenom = forms.CharField (label="Prenom", max_length=30)
	nom = forms.CharField (label="Nom", max_length=30)
	email = forms.EmailField (label="Adresse mail")

class ProfilForm(forms.Form):
	prenom = forms.CharField (label="Prenom", max_length=30, required=False)
	nom = forms.CharField (label="Nom", max_length=30, required=False)
	email = forms.EmailField (label="Adresse mail", required=True)
	img = forms.ImageField (label="Avatar", required=False)
	bio = forms.CharField (label="Bio", widget=forms.Textarea, required=False)
