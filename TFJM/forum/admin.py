from django.contrib import admin
from forum.models import Sujet, Message

class SujetAdmin(admin.ModelAdmin):
	list_display   = ('titre', 'id_topic',)
	search_fields  = ('titre',)
  
class MessageAdmin(admin.ModelAdmin):
	list_display   = ('id_message', 'auteur', 'sujet',) #'date_creation')
	ordering       = ('id_message', )#'date_creation',)
	search_fields  = ('auteur', 'sujet',)
   
admin.site.register (Sujet, SujetAdmin)
admin.site.register (Message, MessageAdmin)
