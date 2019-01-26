from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url="/authenticate/login/")
def index_agregar(request):
    return render(request, 'autenticar/base.html')