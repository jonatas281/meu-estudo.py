import os 
os. system("cls || clear")

"""Crie uma função que receba 5 números e usando uma função,
mostre uma mensagem com a média destes cinco  números informados.
"""
def calcular_media (numero1,numero2,numero3,numero4,numero5):
    resultado = (numero1 + numero2 + numero3 + numero4 + numero5) / 5
    return resultado

numero1 = float(input("digite seu primeira nota: "))
numero2 = float(input("digite sua segunda nota: "))
numero3 = float(input("digite sua terceira nota: "))
numero4 = float(input("digite sua quarta nota: "))
numero5 = float(input("digite sua quinta nota: "))

media_resultado = calcular_media (numero1,numero2,numero3,numero4,numero5)

print(f"sua media é : {media_resultado}")