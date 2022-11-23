from django.shortcuts import render
from agencia.models import *
from agencia.forms import ContactoForm
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def destinos(request):
    return render(request,'destinos.html')

def busqueda(request):
    if "buscar" in request.GET and request.GET["buscar"]:
        consulta= request.GET["buscar"]
        viajes = Viaje.objects.filter(destino__contains=consulta)
        return render(request, 'resultados.html', {'viajes':viajes},)
    else:
        return render(request, 'resultados.html')

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            asunto = 'Consulta de Viaje'
            contenido = formulario.cleaned_data['mensaje']
            contenido += '\n\n' + 'Comunicarse al correo: ' + formulario.cleaned_data['correo']
            mail = EmailMessage(asunto, contenido, to=['buenosviajesaires@gmail.com'])
            try:
                mail.send() 
                return render(request, 'correo_enviado.html')
            except:
                return render(request, 'correo_no_enviado.html')
    else:
        formulario = ContactoForm()
        return render(request, 'contacto.html', {'formulario': formulario})

def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        try:
            formulario.save()
            return render(request, 'usuario_agregado.html')
        except:
            return render(request, 'usuario_no_agregado.html', {'formulario': formulario})
    else:
        formulario = UserCreationForm()
        return render(request, 'registro_usuario.html', {'formulario': formulario})

@login_required(login_url='/ingresar')


def privado(request):
    usuario = request.user
    return render(request, 'privado.html', {'usuario': usuario})

def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/privado')
    elif request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request , acceso)
                    return HttpResponseRedirect('/privado')
            else:
                return render(request, 'no_usuario.html', {'formulario': formulario})   
    else:
        formulario = AuthenticationForm()
        return render(request, 'ingresar.html', {'formulario': formulario})

def salir(request):
    if not request.user.is_anonymous:
            logout(request)
            return HttpResponseRedirect('/ingresar')
    else:
        return HttpResponseRedirect('/ingresar')