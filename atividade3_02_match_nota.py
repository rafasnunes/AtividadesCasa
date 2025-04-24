# Na escola Técnica Soares Lisboa, os estudantes realizam duas avaliações
# principais ao longo do semestre. Além disso, eles têm a opção de realizar
# uma prova optativa, que pode ser utilizada para substituir a menor nota das
# duas avaliações principais, com o objetivo de melhorar a média final.

# Nem todos os estudantes realizam a prova optativa. Quando um estudante não
# realiza essa avaliação, o valor informado para essa nota será -1.

# Calcular a média do semestre considerando que a prova optativa, substitui a
# nota mais baixa entre as duas primeiras avaliações.  

# Escrever a média e mensagens, que indiquem, se o estudante foi aprovado,
# reprovado ou se está em exame, de acordo com as informações abaixo:  

# Aprovado: média >= 6.0,  
# Reprovado: média < 3.0,  
# Exame: média >= 3.0 e < 6.0.  

# Tarefa: 

# Escreva um programa em Python que: 
# Leia as notas das duas avaliações principais e a nota da prova optativa. 
# Calcule a média final do estudante, considerando a substituição da menor nota, se aplicável. 
# Exiba a média calculada. 
# Informe a situação final do estudante: Aprovado, Reprovado ou Exame. 

av1 = float(input('Digite a nova da AV1: '))
av2 = float(input('Digite a nota da AV2: '))
avx = float(input('Digite a nota da AVX (Ou -1 se não fez): '))

if avx != -1:
    if av1 < av2:
        av1 = avx
    else:
        av2 = avx

media = (av1 + av2) / 2

print(f'Nota 1: {av1}')
print(f'Nota 2: {av2}')

print(media)

match media:
    case m if m >= 6:
        print('Aluno Aprovado!')
    case m if m >= 3:
        print('Aluno em Recuperação!')
    case _:
        print('Aluno Reprovado!')
        