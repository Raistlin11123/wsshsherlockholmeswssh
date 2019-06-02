#all the imports needed
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profil, Clue, UserClues
from .forms import LoginForm, ConnexionForm, NewClueForm
from django.contrib.auth.models import User
from django.contrib import messages
import re

#will use a generic view (directly in the url file) for the three next functions below
def index(request):
	return render(request, 'investigation1/index.html', locals())

def scenario(request):
	return render(request, 'investigation1/scenario.html', locals())

def rules(request):
	return render(request, 'investigation1/rules.html', locals())


#function for the connexion of the user. I don't use the name login because it's already used by the auth library
def login_view(request):
	error = False

	

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # We check wither the data are correct
			if user:  # If the object returned is not None
        	    		login(request, user)  # We log the user in.
            		# Otherwise, an error is displayed
			else:
               			error = True
	else:
        	form = LoginForm()

	if request.user.is_authenticated:
		messages.success(request, 'Bienvenu, ami de Sherlock!')
		return redirect('list_clues') #redirection si la connexion s'est bien effectué. Il doit y avoir un moyen plus simple. A chercher


	return render(request, 'investigation1/login.html', locals())

@login_required
def list_clues(request):
	#Formulaire pour un nouvel indice
	if request.method == "POST":
		form = NewClueForm(request.POST)
		#si le formulaire est valide, on enregistre l'indice correspondant sur le user connecté
		if form.is_valid():
			newClue = UserClues()
			newClue.player = request.user
			#Message d'erreur si le nombre rentré n'est pas dans les chiffre de la base

			#-------------------Gestion erreurs----------------------

			present = False
			for y in Clue.objects.filter(number = form.cleaned_data["number"]):
				if y.number == form.cleaned_data["number"]:
					present = True

			if present: #si le nombre existe bien dans la base
				newClue.clue = Clue.objects.get(number = form.cleaned_data["number"])

			else:				
				messages.error(request, 'Cette indice n\'est pas valide')
				return redirect('list_clues')
				#redirect



			##Vérif des doublons pour ne pas surcharger la base et ne pas mettre deux fois le meme indice##
			doublon = False

			for x in UserClues.objects.filter(player = request.user):
				if newClue.clue == x.clue:
					doublon = True

			if doublon:
				messages.error(request, 'vous avez déjà tapé cet indice. Vous pouvez le revoir dans la liste ci-dessous.') #message d'erreur Puis rediredt list
			else:
				newClue.save()

				#redirection vers l'indice tapé si il n'y a pas de doublon
				return redirect('content_clue', id_clue=newClue.id)
				#-----------------------------------------------------------------

			form = NewClueForm()#remise à blanc
			###################################

			

	else:
		form = NewClueForm()

    #Affichage de la liste des indices
	clues = UserClues.objects.filter(player = request.user)
    #mettre un order by avec la date de parution de l'indice


	return render(request, 'investigation1/list_clues.html', {'clues':clues, 'form': form})

@login_required
def content_clue(request, id_clue):
	#On sélectionne l'indice dont l'id à été choisi
	messages.warning(request, 'Votre dernière destination : {}'.format(UserClues.objects.get(id=id_clue).clue.title)) #On prepare un message afficher lors de l'actualisation de la page (quand il sera revenu sur la liste)

	try:
		whole_clue = UserClues.objects.get(id=id_clue)
	except whole_clue.DoesNotExist:
		raise Http404
	#On fait du nombre une chaine de caracter pour la mettre dans l'url de l'image
	number = str(whole_clue.clue.number)
    #-------------------------------------------------
    #On retourne l'indice complet
	return render(request,'investigation1/content_clue.html',{'whole_clue':whole_clue,'number':number}, )






























def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'investigation1/connexion.html', locals())




#function for the login out (very easy) (useless)
def logout_view(request):
    	logout(request)
    	redirect('list_clues')
	#We redirect the user on the connexion page
