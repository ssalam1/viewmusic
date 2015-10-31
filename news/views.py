from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.forms import ModelForm
from news.models import *
# Create your views here.
def creatartist(request):
	if request.method == "GET":
		form = ArtistForm()
		return render (request, 'create.html',{'form':form})
	elif request.method == "POST":
		form = ArtistForm(request.POST)	
		form.save()
		return HttpResponseRedirect('/artists')

def home(request):
	"""docstring for home"""
	artists= Artist.objects.all().order_by('year_formed')
	return render_to_response ('all.html',{'artists':artists})
def index(request):
	
	return render_to_response ('index.html')
def details(request, id):
	artist = Artist.objects.get(pk = id)	
	return render_to_response ('artist.html',{'artist':artist})

def notfound(request):
	return render_to_response ('notfound.html')
