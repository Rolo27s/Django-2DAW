from django.http import HttpResponse

def funcionej1(request, base, altura):
    area = float(base) * float(altura) / 2
    respuesta = (f"El triangulo de base {base} y altura {altura} tiene un area de {area:.2f}")
    return HttpResponse(respuesta)
