import os
os . system ("cls || clear ")

"""Crie uma função que receba 2 números e usando uma função,
mostre uma mensagem com a média destes dois números informados.
"""

def calcular_media (numero1,numero2):
    resultado = (numero1 + numero2) / 2
    return resultado

#solicitar os numeros ao usuario 
numero1 = float(input("digite seu primeiro numero: "))
numero2 = float(input("digite seu segundo numero: "))

media_resultado = calcular_media(numero1,numero2)


print(f"resultado é :{media_resultado}")