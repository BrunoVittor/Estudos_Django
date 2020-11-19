from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import PersonForm


def person_list(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, 'list.html', context)


def person_new(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


def person_update(request, id):  # sempre no update passamos o parametro id na função
    client = get_object_or_404(Client, pk=id)  # aqui é atribuida a váriavel o model e o id para que seja buscado o objeto
    form = PersonForm(request.POST or None, instance=client)  # aqui é atribuido o form.py criado, o método de requisição ou nenhum e a instancia criada acima
    if form.is_valid():
        form.save()
        return redirect('person_list')  # aqui é feito o redirecionamento após salvo o form
    return render(request, 'person_form.html', {'form': form})


def person_delete(request, id):
    client = get_object_or_404(Client, pk=id)
    form = PersonForm(request.POST or None, instance=client)
    if request.method == 'POST':
        client.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'form': form})
