from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request,'index.html', {})

def cart(request, *args, **kwargs):
    return render(request, 'cart.html', {})