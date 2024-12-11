import os 
os. system ("cla || clear")

"""
faça um codigo que pessa ao usuario o login e a senha, se o login e senha estiver correto 
escreva bem vindo se nao escreva erro.
"""


login_salvo = "jonas"
senha_salvo = "12345"

while True: 
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")
    if login == "jona" and senha == "12345":
     print ("bem vindo")
     break
    else:
     print("erro:")
    