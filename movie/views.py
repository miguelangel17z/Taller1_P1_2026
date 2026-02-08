from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home.html",{'name':'Kanye West'});

def about(request):
    return HttpResponse("Bro");


# Create your views here.
