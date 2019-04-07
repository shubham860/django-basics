from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1 style='background-color:black;color:white;'>First Django application</h1>")
