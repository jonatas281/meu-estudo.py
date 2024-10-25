import os 
os . system ("cls || clear")
# Inicializa listas e variáveis
dados = []
soma_salarios = 0
quantidade_mulheres_acima_5000 = 0

def adicionar_pessoa():
    global soma_salarios, quantidade_mulheres_acima_5000 
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    salario = float(input("Digite o salário: "))

    # Adiciona os dados à lista
    dados.append((idade, sexo, salario))
    
    # Atualiza a soma dos salários
    soma_salarios += salario
    
    # Conta mulheres com salário acima de R$ 5.000,00
    if sexo == 'F' and salario >= 5000:
        quantidade_mulheres_acima_5000 += 1

def exibir_resultados():
    if not dados:
        print("Nenhum dado foi registrado.")
        return

    # Cálculo da média de salário
    media_salario = soma_salarios / len(dados)

    # Cálculo da maior e menor idade
    idades = [idade for idade, sexo, salario in dados]
    maior_idade = max(idades)
    menor_idade = min(idades)

    # Exibe os resultados
    print(f"Média de salário do grupo: R$ {media_salario:.2f}")
    print(f"Maior idade do grupo: {maior_idade} anos")
    print(f"Menor idade do grupo: {menor_idade} anos")
    print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres_acima_5000}")

def main():
    while True:
        print("\nMenu:")
        print("1 - Adicionar pessoa")
        print("2 - Exibir resultados e sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_pessoa()
        elif opcao == '2':
            
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()