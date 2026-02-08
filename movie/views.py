from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home.html",{'name':'Miguel Garcia'});

def about(request):
    return HttpResponse("Bro");


# Create your views here.
