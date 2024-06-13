from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def register(request):
    return render(request, 'register.html')
