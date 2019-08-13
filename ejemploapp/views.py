from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    respu = "<ul>"
    respu = respu + "<li>elemento1</li>"
    respu = respu + "<li>elemento2</li>"
    respu = respu + "</ul>"

    return  HttpResponse(respu)


def nuevococinero(request):
    return HttpResponse("<p>esta es la pagina nuevo cocinero</p>")

def vercliente(request):
    return HttpResponse("<h1>esta es la pagina de ver clientes</h1>")

def verfactura(request):
    return HttpResponse("<h1>esta es la pagina de ver facturas</h1>")

def vermesero(request):
    return HttpResponse("<h1>esta es la pagina de ver meseros</h1>")
