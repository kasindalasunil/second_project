from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Jampandu(request):
    return HttpResponse('<h1><marquee>hi how are you</h1></marquee>')

def Jigelrani(request):
    return HttpResponse('<h1><marquee>reply:i will give you whatever you ask<h1><marquee>')
