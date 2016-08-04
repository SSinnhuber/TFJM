from django import forms

class ReponseForm (forms.Form):
	reponse = forms.CharField (label="Votre reponse", widget=forms.Textarea)

class SujetForm (forms.Form) :
	titre = forms.CharField (label="Titre du sujet", max_length=30)
	message = forms.CharField (label="Votre message", widget=forms.Textarea)
