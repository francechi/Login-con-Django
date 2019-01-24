from django.urls import path, include, re_path
from aplicaciones.programa.views import index, programa_view
from . import views

urlpatterns = [
    path('programa/', views.index, name='index'),
    path('programa/nuevo/', views.programa_view, name='programa_crear')

]