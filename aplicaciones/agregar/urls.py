from django.urls import path, include, re_path
from aplicaciones.agregar.views import index_agregar

urlpatterns = [
    path('agregar', index_agregar),

]