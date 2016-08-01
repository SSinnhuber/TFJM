from django.contrib import admin
from profils.models import Profil

class ProfilAdmin(admin.ModelAdmin):
   list_display   = ('id', 'user', 'img')
   ordering       = ('id', )
   search_fields  = ('user',)
   
admin.site.register (Profil, ProfilAdmin)
