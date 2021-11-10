from django.shortcuts import render

def index(request):
    return render(request, '3D/index.html')