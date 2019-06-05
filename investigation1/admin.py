from django.contrib import admin
from .models import Profil, Clue, UserClues
# Register your models here.

class ClueAdmin(admin.ModelAdmin):
    list_display   = ('title', 'number',)
    ordering       = ('title', 'number')

class UserCluesAdmin(admin.ModelAdmin):
    list_display   = ('player', 'clue',)
    list_filter    = ('player', 'clue')
    ordering       = ('player', 'clue')
    search_fields  = ('player', 'clue')


admin.site.register(Profil)
admin.site.register(Clue, ClueAdmin)
admin.site.register(UserClues, UserCluesAdmin)

#Ajouter des tris