from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicaciones.autenticar.urls')),
    path('', include('aplicaciones.programa.urls')),
    path('', include('aplicaciones.agregar.urls'))
]