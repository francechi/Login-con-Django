from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ProgramaForm
from .models import Programa
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/authenticate/login/")
def index(request):
    return render(request, 'programa/index.html')

@login_required(login_url="/authenticate/login/")
def programa_view(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('programa_list')
    else:
        form = ProgramaForm()

    return render(request, 'programa/programa_forms.html', {'form': form})

@login_required(login_url="/authenticate/login/")
def programa_list(request):
    programa = Programa.objects.all().order_by('id')
    contexto = {'programa': programa}
    return render(request, 'programa/programa_list.html', contexto)

@login_required(login_url="/authenticate/login/")
def programa_delete(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    if request.method == 'POST':
        programa.delete()
        return redirect('programa_list')
    return render(request, 'programa/programa_delete.html', {'programa': programa})

@login_required(login_url="/authenticate/login/")
def programa_edit(request, programa_id):
    programa = Programa.objects.get(pk=programa_id)
    if request.method == 'GET':
        form = ProgramaForm(instance=programa)
    else:
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
                form.save()
        return redirect('programa_list')
    return render(request, 'programa/programa_forms.html', {'form': form})
