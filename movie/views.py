from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home.html",{'name':'Kanye West'});

def about(request):
    return render(request,"About.html");


# Create your views here.
