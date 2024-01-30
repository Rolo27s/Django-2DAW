from django import forms

class FormularioContacto(forms.Form): # Django usa como parámetro la clase Padre
    nombre = forms.CharField()
    telefono = forms.IntegerField(required=False)
    email = forms.EmailField()
    web = forms.URLField(required=False, label="URL web")
    mensaje = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':'7', 'cols':'20'}
        )
    )
