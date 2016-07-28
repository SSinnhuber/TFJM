from django.contrib import admin
from infos.models import Categorie, Sscategorie, Article, Lien

class ArticleAdmin(admin.ModelAdmin):
   prepopulated_fields = {"slug": ("titre",)}
   list_display   = ('titre', 'sscat', 'date', 'slug')
   list_filter    = ('sscat',)
   date_hierarchy = 'date'
   ordering       = ('sscat', )
   search_fields  = ('titre', 'contenu')
   
class LienAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'adresse', 'lienhttp', 'sscat', 'isLienhttp')
   list_filter    = ('sscat',)
   ordering       = ('sscat', )
   search_fields  = ('titre',)

class SscategorieAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'cat', 'image')
   list_filter    = ('nom', 'cat')
   ordering       = ('nom',)
   search_fields  = ('nom',)

class CategorieAdmin(admin.ModelAdmin):
	list_display   = ('nom', 'image')
	prepopulated_fields = {"slug": ("nom",)}
	
admin.site.register (Categorie, CategorieAdmin)
admin.site.register (Sscategorie, SscategorieAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register (Lien, LienAdmin)
