from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def main (reqruest):
    return render(reqruest, 'index.html')


def dashboard (reqruest):
    return render(reqruest, 'dashboard/index.html')

# About me
def about_me_list(request):
    context = models.About_me.objects.all()
    return render(request, 'dashboard/about_me/index.html', {'context':context})


def about_me_create(request):
    if request.method == 'POST':
        models.About_me.objects.create(
            text = request.POST['text']
        )
        return redirect('about_me_list')
    return render(request, 'dashboard/about_me/create.html')


def about_me_deteil(request, id):
    context = models.About_me.objects.get(id=id)
    if request.method == "POST":
        context.text = request.POST['text']
        context.save()
        return redirect('about_me_list')
    return render(request, 'dashboard/about_me/deteil.html', {'context':context})


def about_me_delete(request, id):
    models.About_me.objects.get(id=id).delete()
    return redirect('about_me_list')


# Equpment
def equpment_list(request):
    context = models.My_equpment.objects.all()
    return render(request, 'dashboard/equpment/index.html', {'context':context})


def equpment_deteil(request, id):
    context = models.My_equpment.objects.get(id=id)
    if request.method == "POST":
        context.name = request.POST['name']
        context.save()
        return redirect('equpment')
    return render(request, 'dashboard/equpment/deteil.html', {'context':context})

def equpment_create(request):
    if request.method == 'POST':
        models.My_equpment.objects.create(
            name = request.POST['name']
        )
        return redirect('equpment')
    return render(request, 'dashboard/equpment/create.html')

def equpment_delete(request, id):
    models.My_equpment.objects.get(id=id).delete()
    return redirect('equpment')