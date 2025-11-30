"""Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

Exemplo de entrada:


Digite o primeiro número: 10   
Digite o segundo número: 5   
Escolha a operação (| + | - | * | / |): + 
Copiar código
Saída esperada:


O resultado é: 15 """

def calcular(num1: float, num2: float, operador: str) -> float:
    """Realiza uma operação matemática básica entre dois números usando funções lambda.

    Parâmetros:
    - num1: o primeiro número (float)
    - num2: o segundo número (float)
    - operador: uma string representando a operação ('+', '-', '*', '/')

    Retorna:
    - o resultado da operação (float)

    Levanta ValueError se o operador for inválido ou se houver tentativa de divisão por zero.
    """
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ValueError("Divisão por zero não é permitida"))
    }

    if operador not in operacoes:
        raise ValueError(f"Operador inválido: {operador}. Use '+', '-', '*', ou '/'.")

    return operacoes[operador](num1, num2)
if __name__ == "__main__":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operador = input("Escolha a operação (| + | - | * | / |): ").strip()

        resultado = calcular(num1, num2, operador)
        print(f"O resultado é: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
"""""""""
Lara está gerenciando o estoque de sua loja e recebeu duas listas separadas:    
uma contendo os nomes dos produtos e outra com seus respectivos preços.
Crie um programa que junte as listas e exiba o resultado no formato
produto: preço. A função aceita as listas como parâmetros e retorna uma 
lista contendo as strings formatadas.
Comportamento:
- pareia cada produto ao preço correspondente na mesma posição;
- se as listas tiverem tamanhos diferentes, empareia até o menor tamanho
  e informa quantos itens ficaram sem par.      """
from typing import List, Sequence
def juntar_listas(produtos: Sequence[str], precos: Sequence[float]) -> List[str]:
    """Combine duas sequências (produtos e preços) e retorne uma lista de
    strings no formato 'produto: preço'.

    Parâmetros
    - produtos: sequência de nomes de produto (str)
    - precos: sequência de preços (float ou valores que suportem str())

    Retorna
    - lista de strings formatadas 'produto: preço'.

    Observação: a combinação é feita até o menor comprimento entre as duas
    sequências. Se existirem itens sem par, não são incluídos no resultado.
    """
    resultado: List[str] = []
    menor = min(len(produtos), len(precos))

    for i in range(menor):
        produto = produtos[i]
        preco = precos[i]
        resultado.append(f"{produto}: {preco}")

    # informar casos em que há itens sem par
    if len(produtos) != len(precos):
        # não alteramos o resultado — apenas documentamos a diferença
        diff = abs(len(produtos) - len(precos))
        if len(produtos) > len(precos):
            print(f"Aviso: {diff} produto(s) sem preço correspondente.")
        else:
            print(f"Aviso: {diff} preço(s) sem produto correspondente.")

    return resultado        