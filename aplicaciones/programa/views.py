from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ProgramaForm
from .models import Programa
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'programa/index.html')

def programa_view(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('programa_list')
    else:
        form = ProgramaForm()

    return render(request, 'programa/programa_forms.html', {'form':form})


def programa_list(request):
    programa = Programa.objects.all()
    contexto = {'programa':programa}
    return render(request, 'programa/programa_list.html', contexto)

def programa_delete(request, programa_id):
    programa = Programa.objects.get(pk=programa_id)
    programa.delete()
    messages.success(request, ('Programa Eliminado!'))
    return redirect('programa_list')
