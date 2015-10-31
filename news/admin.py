from django.contrib import admin
from news.models import *
class ArtistAdmin(admin.ModelAdmin):
	"""docstring for ArtistAdmin"""
	list_display = 'name',
	prepopulated_fields = {'year_formed': ('name',)}
class AlbumAdmin(admin.ModelAdmin):
	"""docstring for ArtistAdmin"""
	list_display = 'name',
	

# Register your models here.
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Album,AlbumAdmin)
