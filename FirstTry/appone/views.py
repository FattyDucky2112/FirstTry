from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"appone/index.html")

def pics(request):
    return render(request,"appone/pics.html")
