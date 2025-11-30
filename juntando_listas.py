"""Juntar listas de produtos e preços.

Lara está gerenciando o estoque de sua loja e recebeu duas listas separadas:
uma contendo os nomes dos produtos e outra com seus respectivos preços.

Crie um programa que junte as listas e exiba o resultado no formato
produto: preço. A função aceita as listas como parâmetros e retorna uma
lista contendo as strings formatadas.

Comportamento:
- pareia cada produto ao preço correspondente na mesma posição;
- se as listas tiverem tamanhos diferentes, empareia até o menor tamanho
  e informa quantos itens ficaram sem par.
"""

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


if __name__ == "__main__":
	# Exemplo de uso
	produtos_ex = ["Camisa", "Calça", "Meias"]
	precos_ex = [49.99, 89.9, 9.5]

	pares = juntar_listas(produtos_ex, precos_ex)
	for linha in pares:
		print(linha)




