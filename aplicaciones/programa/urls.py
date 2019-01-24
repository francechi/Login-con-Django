from django.urls import path, include
from aplicaciones.programa.views import index

urlpatterns = [
    path('programa', index),
]