# respuestas con stings
from django.http import HttpResponse

from django.template import Template, Context, loader

from datetime import datetime

def hello(request):
    
    return HttpResponse("Hola coders")
    
def say_hello_with_name(request, name):

    return HttpResponse(f"Hola {name}")

def print_add(request, num1, num2):

    return HttpResponse(f"{num1} + {num2} = {num1+num2}")

def index(request, nombre):
    #0 crear un contexto
    datos_contexto = {"fecha_actual": datetime.now(), "username": nombre}

    #1 cargar contendio
    archivo = open(r"C:\Users\Leandro\Leandro\Leandro Personal\Cursos\Python\DJANGO1\ecommerce\ecommerce\templates\index.html")
    contenido_html = archivo.read()
    archivo.close()

    #2 cracion de planitlla
    plantilla = Template(contenido_html)

    #3 crear contexto
    contexto = Context(datos_contexto)

    #4 armar la documento para renderizar
    documento_a_renderizar = plantilla.render(contexto)

    #5 devolve rrespuesta a usuario
    return HttpResponse(documento_a_renderizar)

def notas(request):
    # crear contexto
    datos = {"notas": [9,4,6,7,10], "estudiante": "Leandro"}

    # cargar contenido html
    archivo = open(r"C:\Users\Leandro\Leandro\Leandro Personal\Cursos\Python\DJANGO1\ecommerce\ecommerce\templates\notas.html", "r")
    contenido = archivo.read()
    archivo.close()

    # crear plantilla
    plantilla = Template(contenido)

    # crear el contexto
    contexto = Context(datos)

    #renderizar el html con la informacion del contexto
    documento = plantilla.render(contexto)

    # retornar el documento como respuesta
    return HttpResponse(documento)
    

def alumnos(request):
    
    datos = {"curso": "python", "alumnos": ["Leonel", "Pedro", "Santiago", "Maria"]}
    
    plantilla = loader.get_template("alumnos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)


