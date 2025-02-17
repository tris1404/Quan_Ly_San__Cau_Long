from django.shortcuts import render
from django.http import HttpResponse
from app_admin.models import Court
from django.template import loader

def Customer(request):
    return HttpResponse("Hello world!")


def home(request):
    return render(request, 'home.html')


def courts(request):
    courts = Court.objects.all()
    template = loader.get_template('app_home/court/courts.html')
    context = {
        'court': courts,
    }
    return HttpResponse(template.render(context, request))


def courtEdit(request):
    courts = Court.objects.all()
    template = loader.get_template('app_home/court/court-edit.html')
    context = {
        'court': courts,
    }
    return HttpResponse(template.render(context, request))

def courtBooking(request):
    courts = Court.objects.all()
    template = loader.get_template('app_home/court/court-booking.html')
    context = {
        'court': courts,
    }
    return HttpResponse(template.render(context, request))
