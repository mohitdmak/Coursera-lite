from django.shortcuts import render

def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')