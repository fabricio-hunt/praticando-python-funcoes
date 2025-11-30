"""Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total."""

def total_de_vendas():
    vendas = input("Digite os valores das vendas separadas por espaço: ")
    lista_vendas = vendas.split()
    
    total = 0
    for venda in lista_vendas:
        total += float(venda)
    
    print(f'O total de vendas é: R$ {total:.2f}')

total_de_vendas()