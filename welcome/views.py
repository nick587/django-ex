import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse

from . import database
from .models import PageView
from django.template.context_processors import request

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def helloMessage(request):
    return JsonResponse({"message" : "Ehyl� gente!!!!!"})