from django.shortcuts import render, redirect
from .models import Client
from .forms import PersonForm


def person_list(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, 'list.html', context)


def person_new(request):
    form = PersonForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})
