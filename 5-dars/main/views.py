from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

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