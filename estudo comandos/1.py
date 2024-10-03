import os 
os . system ("cls || clear")

# declarando variaveis
nota=3
media = 0

# solicitando dados 
for i in range(3):
    nota=int(input(f"digite sua {i+1} nota:"))

#calculando

media = nota + nota / 3

# exibindo dados
print(f"nota: {nota}") 
print(f"media: {media}")

