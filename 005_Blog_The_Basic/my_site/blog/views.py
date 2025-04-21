from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def posts(request):
    return HttpResponse("Hello, world. You're at Posts Page")

def post_detail(request,slug):
    return HttpResponse("Hello, world. You're at Post Detail Page " +slug)