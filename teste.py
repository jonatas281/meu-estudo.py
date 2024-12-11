import os 
os. system ("cls || clear")

# quardando dados 
login_salvo = "jona"
senha_salvo = "12345"

# solicitando dados 
while True:
  login = input("digite seu login: ")
  senha = input("digite sua senha: ")

  if login == "jona" and senha == "12345":
    print ("bem vindo ")
    break
  else:
    print("login e senha errado:") 
