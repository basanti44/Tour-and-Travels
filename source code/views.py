from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'velora/home.html')

def about(request):
    return render(request, 'velora/about.html')

def contact(request):
    return render(request, 'velora/contact.html')

def destinations(request):
    return render(request, 'velora/destination.html')