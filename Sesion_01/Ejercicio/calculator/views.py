"""Calculadora Views"""

from django.http import JsonResponse

def calculadora(request, operacion, a, b):
    if operacion == "suma":
        result = a + b
        result = "La suma de {} + {} = {}".format(a, b, result)
        message = {
            "result": result
        }
    elif operacion == "resta":
        result = a - b
        result = "La resta de {} - {} = {}".format(a, b, result)
        message = {
            "result": result
        }
    elif operacion == "multiplicacion":
        result = a * b
        result = "La multiplicacion de {} * {} = {}".format(a, b, result)
        message = {
            "result": result
        }
    elif operacion == "division":
        if b == 0:
            print ("Error: División entre 0")
        else:
            result = a / b
            result= "La division de {} / {} = {}".format(a, b, result)
        message = {
            "Repsuesta": result
        }
    return JsonResponse(message)

