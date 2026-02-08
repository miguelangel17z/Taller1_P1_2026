from django.shortcuts import render
from django.http import HttpResponse
from .models import movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = movie.objects.all()
    return render(request,"home.html",{'searchTerm': searchTerm, 'movies': movies});

def about(request):
    return render(request,"About.html");


# Create your views here.
