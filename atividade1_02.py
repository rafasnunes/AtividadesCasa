# Você foi convidado/a a desenvolver um sistema para avaliar o desempenho das vendas dos vendedores em uma loja.  

# Em conversa com o gestor de vendas, você foi informado/a que o sistema deve classificar o desempenho dos vendedores com base na quantidade de unidades vendidas durante o mês, seguindo estas regras: 

# Excelente: 100 unidades ou mais. 
# Bom: entre 70 e 99 unidades. 
# Regular: entre 30 e 69 unidades. 
# Insuficiente: menos de 30 unidades. 

# Após realizar essa classificação, informar qual nível (Excelente, Bom, Regular ou Insuficiente) o/ vendedor/a se encontra. 

# É essencial que o sistema possibilite que o gestor digite a quantidade de unidades vendidas por um/a vendedor/a. 

nome = input(f'Digite o nome do vendedor: ')
vendas = int(input('Digite a quantidade de vendas no mês: '))

if vendas >= 100:
    print(f'O ranking do vendedor {nome} é excelente!')
elif vendas >= 70:
    print(f'O ranking do vendedor {nome} é bom!')
elif vendas >=30:
    print(f'O ranking do vendedor {nome} é regular!')
else:
    print(f'O ranking do vendedor {nome} é insuficiente!')