from django.http import HttpResponse, HttpResponseBadRequest
import datetime
from django.views.decorators.http import require_GET
from django.template.loader import get_template

def holamundo(request):
    return HttpResponse("<p>Hola mundo desde Django</p>")

def ahora(request):
    ahora = datetime.datetime.now()
    formatted_time = ahora.strftime("%H:%M:%S")
    html = "<p>Son las " + formatted_time + "</p>"
    return HttpResponse(html)

@require_GET # Todo esto es para tratar de controlar las excepciones pero no consigo hacerlo
def par(request, num):
    try:
        num = int(num)  # Intentar convertir el parámetro en un entero
        if num % 2 == 0:
            return HttpResponse(f"El número {num} es par")
        else:
            return HttpResponse(f"El número {num} es impar")
    except ValueError:
        return HttpResponseBadRequest("Por favor, ingrese un número válido.")

def es_par(request, num):
    if num % 2 == 0:
        texto = str(num) + " es par"
    else:
        texto = str(num) + " es impar"

    plantilla = get_template("par.html")
    datoscontexto = { "texto":texto }
    return HttpResponse(plantilla.render(datoscontexto))
