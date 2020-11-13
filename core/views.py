from django.shortcuts import render
from .models import Client


def list(request):
    context = {
        "clients": Client.objects.all()
    }
    return render(request, 'list.html', context)
