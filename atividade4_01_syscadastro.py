# Sua Tarefa: 

# Desenvolver um programa em Python, que recebe 10 candidatos. 
# Para os candidatos, que serão “cadastrados” o algoritmo deve solicitar: 

# Nome 
# Ano de nascimento (ex: 2006) 
# Telefone 
# E-mail 
# Formação acadêmica 
# Experiência profissional  

# Importante: 

# Candidatos menores de 18 anos não podem ser cadastrados. Se a pessoa tiver menos de 18 anos, exiba mensagem negando: 
# Calcule a idade com base no ano atual (2025). 
# O sistema só deve receber 10 candidatos apenas. 
# Use estruturas de repetição e decisão para controlar o fluxo. 

i = 1

while i <= 10:

    nome = input(f'Insira o nome do Aluno {i}: ')
    ano_nasc = int(input(f'Digite o ano do nascimento: '))
    telefone = input(f'Digite o telefone de contato: ')
    email = input(f'Digite o e-mail: ')
    formacao = input(f'Digite a formação do aluno: ')
    profissional_xp = input(f'Digite a experiência profissional: ')
    
    if (2025 - ano_nasc) < 18 :
        print(f'Aluno {nome} não pode ser cadastrado por ser menor de 18 anos.')
    else:
        print(f'Aluno {nome} cadastrado com sucesso!')
        i = i + 1