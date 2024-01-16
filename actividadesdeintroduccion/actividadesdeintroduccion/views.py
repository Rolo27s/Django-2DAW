from django.http import HttpResponse
from django.template.loader import get_template

def funcionej1(request, base, altura):
    area = base * altura / 2
    respuesta = (f"El triangulo de base {base} y altura {altura} tiene un area de {area:.2f}")
    return HttpResponse(respuesta)

# funcion del ejercicio 2 desarrollada con GET
def funcionej2(request):
    lado1 = request.GET.get('lado1', None);
    lado2 = request.GET.get('lado2', None);

    if(lado1 == None or lado2 == None):
        respuesta = ("Estas accediendo al back por un método GET el cual tiene dos query params llamados: lado1 y lado2")
    else:
        area = float(lado1) * float(lado2)
        respuesta = (f"El rectángulo de lado1 {lado1} y lado2 {lado2} tiene un area de {area:.2f}")
    return HttpResponse(respuesta)

def ejemplo2(request, nombre):
    html = get_template("Ej1.html")
    datos = {
        "nomb_persona":nombre,
        "positivo": len(nombre)>=8,
        "lista": [1,5,"a",6],
        }
    return HttpResponse(html.render(datos))
