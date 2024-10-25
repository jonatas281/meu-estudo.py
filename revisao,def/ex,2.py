import os
os . system ("cls || clear")

"""Crie funções que receba 2 números e retorne a soma, subtração, divisão
e a multiplicação destes dois números informados.

Obs.: Crie uma função para cada operação.
"""
def soma (numero1,numero2):
    resultado = numero1 + numero2
    return resultado
def subtracao (numero1,numero2):
    resultado = numero1 - numero2
    return resultado
def multiplicacao (numero1,numero2):
    resultado = numero1 * numero2
    return resultado
def divisao (numero1,numero2):
    if numero2 !=0:
        resultado = numero1 / numero2
    else:
        resultado =  "erro divisao por zero "
    return resultado

numero1 = float(input("digite seu primeiro numero: "))
numero2 = float(input("digite seu segundo numero: "))

resultado_soma = soma(numero1,numero2)
resultado_subtracao = subtracao(numero1,numero2)
resultado_multiplicacao = multiplicacao(numero1,numero2)
resultado_divisao = divisao(numero1,numero2)

print(f"resultado da soma: {resultado_soma}")
print(f"resultado da subtração: {resultado_subtracao}")
print(f"resoltado da multiplicação: {resultado_multiplicacao}")
print(f"resultaddo da divisão: {resultado_divisao}")