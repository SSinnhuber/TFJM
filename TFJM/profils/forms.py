from django import forms


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
