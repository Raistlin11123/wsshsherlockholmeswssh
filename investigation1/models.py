from django.db import models
from django.contrib.auth.models import User

#Class pour les informations sur l'utilisateur
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#Liaison vers le User
    #Informations compplémentaire à ajouter
    
    def __str__(self):
        return "Profil de {}".format(self.user.username)


class Clue(models.Model):
	title = models.CharField(max_length=42, verbose_name='Titre')
	url_img_optionnel =  models.CharField(max_length=42, default= 'rien', verbose_name='url_img_optionnel')#rien si il n'y a pas d'image
	number = models.IntegerField(null=True, verbose_name="numéro")

	def __str__(self):
		return "{}".format(self.title)

class UserClues(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	clue = models.ForeignKey(Clue, on_delete=models.CASCADE)

	def __str__(self):
		return "indice de {}".format(self.player.username)
#trouver un nom singulier autre que UserClue (déjà utilisé par django)