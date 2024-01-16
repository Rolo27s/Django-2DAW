"""
URL configuration for actividadesdeintroduccion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import funcionej1 #, funcionej2, funcionej3, funcionej4, funcionej5, funcionej6, funcionej7, funcionej8, funcionej9, funcionej10

# https://docs.djangoproject.com/en/3.0/topics/http/urls/#registering-custom-path-converters
# int, str, slug, uuid, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ej1/<str:base>/<str:altura>', funcionej1), 
    #path('ej2/', funcionej2),
    #path('ej3/', funcionej3),
    #path('ej4/', funcionej4),
    #path('ej5/', funcionej5),
    #path('ej6/', funcionej6),
    #path('ej7/', funcionej7),
    #path('ej8/', funcionej8),
    #path('ej9/', funcionej9),
    #path('ej10/', funcionej10),
]
