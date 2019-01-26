from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('agregar/', views.index_agregar, name='agregar'),
]