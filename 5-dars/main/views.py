from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def index(request):
    if request.method == 'POST':
        Make_trip.objects.create(
            pick_up_location = request.POST['PICK_UP_LOCATION'],
            drop_off_location = request.POST['DROP_OFF_LOCATION'],
            pick_up_date = request.POST['PICK_UP_DATE'],
            drop_off_date = request.POST['DROP_OFF_DATE'],
            pick_up_time = request.POST['PICK_UP_TIME']
        )
    return render(request, 'main/index.html')

# def create(request):
#     Make_trip.objects.create(
#         pick_up_location = request.POST['PICK_UP_LOCATION'],
#         drop_off_location = request.POST['DROP_OFF_LOCATION'],
#         pick_up_date = request.POST['PICK_UP_DATE'],
#         drop_off_date = request.POST['DROP_OFF_DATE'],
#         pick_up_time = request.POST['PICK_UP_TIME']
#     )

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def car(request):
    return render(request, 'main/car.html')

def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    return render(request, 'main/contact.html')

def blog_single(request):
    return render(request, 'main/blog-single.html')