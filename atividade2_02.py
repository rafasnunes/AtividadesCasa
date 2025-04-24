# A empresa XLWs, especializada em logística precisa identificar
# automaticamente a região de procedência de um produto com base
# no seu código de origem. Cada código representa uma região do
# Brasil, conforme a tabela abaixo:

# Código  # Região

# 1   # Sul
# 2  # Norte
# 3 # Leste
# 4 # Oeste
# 5 ou 6 # Nordeste
# 7, 8 ou 9  # Sudeste
# 10 # Centro-Oeste
# 11 # Noroeste

# Caso o código informado não esteja entre os especificados, o produto deve
# ser classificado como “Importado”.

# Tarefa:

# Escreva um programa em Python que:
# Leia do usuário o código de origem do produto (número inteiro).
# Imprima na tela a região correspondente, de acordo com a tabela acima.
# Caso o código não esteja na lista, informe que o produto é "Importado".

codigo = int(input('Digite o código da região do produto: '))

match codigo:
    case 1:
        print("Região Sul")
    case 2:
        print("Região Norte")
    case 3:
        print("Região Leste")
    case 4:
        print("Região Oeste")
    case 5 | 6:
        print("Região Nordeste")
    case 7|8|9:
        print("Região Sudeste")
    case 10:
        print("Região Centro-Oeste")
    case 11:
        print('Região Noroeste')
    case _:
        print('Produto Importado')
    
print(codigo)