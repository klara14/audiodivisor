"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import generar_planificacion, resultados, dividir_audio, resultados_division 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generar_planificacion, name = 'index'),
    path('resultados', resultados, name = 'resultados'),
    path('dividir_audio', dividir_audio, name = 'dividir_audio'),
    path('resultados_division', resultados_division, name = 'resultados_division')
    
]
