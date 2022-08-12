"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ecommerce.view import hello, say_hello_with_name, print_add, notas, index, alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hello),
    path('hello/<name>/', say_hello_with_name),
    path('suma/<int:num1>/<int:num2>/', print_add),
    path('notas/', notas),
    path('alumnos/', alumnos),
    path('<str:nombre>/', index)
]
