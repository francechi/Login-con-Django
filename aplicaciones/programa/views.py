from django.shortcuts import render, redirect
from django.http import HttpResponse
from aplicaciones.programa.forms import ProgramaForm
# Create your views here.

def index(request):
    return render(request, 'programa/index.html')

def programa_view(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('programa:index')
    else:
        form = ProgramaForm()

    return render(request, 'programa/programa_forms.html', {'form':form})