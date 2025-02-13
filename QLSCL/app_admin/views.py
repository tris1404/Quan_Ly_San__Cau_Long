from django.shortcuts import render
from django.http import HttpResponse

def Court(request):
    return HttpResponse("Hello world!")


def Customer(request):
    return HttpResponse("Hello world!")