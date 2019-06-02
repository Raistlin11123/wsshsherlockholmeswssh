from django import forms
from .models import Profil

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=30, widget= forms.TextInput
                           (attrs={'placeholder':'Entrez votre pseudo'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Entrez votre mot de passe'}))

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class NewClueForm(forms.Form):
	number = forms.IntegerField(label="", widget= forms.NumberInput
                           (attrs={'placeholder':'Entrez le numéro'}))