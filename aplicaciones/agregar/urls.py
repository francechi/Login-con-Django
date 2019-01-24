from django.urls import path, include
from aplicaciones.agregar.views import index_agregar

urlpatterns = [
    path('agregar', index_agregar),

]