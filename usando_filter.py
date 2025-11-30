"""Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter()."""

def usando_filter():
    numeros = input("Digite uma lista de números separados por espaço: ")
    lista_numeros = numeros.split()
    
    numeros_pares = list(filter(lambda x: int(x) % 2 == 0, lista_numeros))
    
    print(f'Números pares: {", ".join(numeros_pares)}')

usando_filter()