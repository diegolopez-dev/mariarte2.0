from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_Contacto=FormularioContacto()
    if request.method=="POST":
        formulario_Contacto=FormularioContacto(data=request.POST)
        if formulario_Contacto.is_valid():
            return redirect("/contacto/?valido")
            
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_Contacto})