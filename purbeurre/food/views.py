from django.shortcuts import render

def index(request):
    return render(request, 'food/index.html')

def result(request):
    return render(request, 'food/result.html')

def detail(request):
    return render(request, 'food/detail.html')

def favorites(request):
    return render(request, 'food/favorites.html')