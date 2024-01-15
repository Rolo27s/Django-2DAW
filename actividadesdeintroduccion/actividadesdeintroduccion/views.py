from django.http import HttpResponse

def funcionej1(request, base, altura):
    area = base * altura / 2
    respuesta = (f"El triangulo de base {base} y altura {altura} tiene un area de {area}")
    return HttpResponse(respuesta)
