from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormularioContacto

def contacto(request):
    if request.method=="POST":
        formCont = FormularioContacto(request.POST)
        if formCont.is_valid():
            infoForm = formCont.cleaned_data # Monta el infoForm en formato JSON
            texto = "Recibido!<br />"
            texto = texto + "Nombre: " + infoForm['nombre'] + "<br /><br />"
            return HttpResponse(str(texto) + str(infoForm) + '<br /><br />' +'<button type="button" onclick="history.back()">Volver</button>')
        else:
            return render(request, "contacto.html", { "form": formCont})
    else:
        return render(request, "contacto.html", {"form":FormularioContacto()})