from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def categori(request):
    return render(request, 'main/categori.html')

def allnews(request):
    return render(request, 'main/allnews.html')