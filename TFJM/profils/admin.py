from django.contrib import admin
from profils.models import Profil

class ProfilAdmin(admin.ModelAdmin):
	list_display   = ('user', 'id', 'img')
	ordering       = ('id', 'user')
	search_fields  = ('user',)
   
admin.site.register (Profil, ProfilAdmin)
