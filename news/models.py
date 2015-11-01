from django.db import models
from django import forms

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=50)
	year_formed = models.PositiveIntegerField()
	details = models.CharField(max_length=4096)

class Album(models.Model):
	name = models.CharField("album",max_length=50)
	artist= models.ForeignKey(Artist)
class ArtistForm(forms.ModelForm):
	"""docstring for Create"""
	class Meta:
		model= Artist
		fields =['name','year_formed','details']
class editform(forms.ModelForm):
	"""docstring for editform"""
	class Meta:
		model = Artist
		fields = ['details']
	