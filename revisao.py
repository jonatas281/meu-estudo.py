import os 
os . system ("cls || clear")

# declarando variaveis 
login =input("digite seu login: ")
senha =input("digite sua senha: ")

login_salvo= login == "jonas"
senha_salva= senha == "1234"

while True:
    login = input ("digite seu login: ")
    senha = input ("digite sua senha: ")

    if login_salvo == login and senha_salva == senha:
     print ("bem vindon ")
    break
print ("tente novamente")
