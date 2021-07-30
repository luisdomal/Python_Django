""" Calculadora views"""

from django.http import HttpResponse, JsonResponse



def hola_django(request):
    """Saluda al usuaio"""

    if "name" in request.GET:
        name = request.GET["name"]
    else:
        name = "Django"

    message = "Hola {}".format(name)
    return HttpResponse(message)


def perfil(request, username):
    """Muestra un perfil de usuario"""
    message = "Hola, @{}".format(username)
    return HttpResponse(message)

def suma(request, a, b):
    """Suma 2 números"""
    resultado = a + b
    return HttpResponse(resultado)

def sumaJson(request, a, b):
    """Suma 2 números"""
    result = a + b
    result = "{} + {} = {}".format(a, b, result)
    message = {
        "result": result
    }
    return JsonResponse(message)

