from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> rediscover blogging </h1>')

def about(request):
    return HttpResponse('<h1>About Bloggr</h1>')
