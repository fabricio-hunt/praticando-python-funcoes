"""Sara está participando de um concurso de escrita, e uma das
 regras exige que cada palavra de seu texto tenha
um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e
 exiba a quantidade de caracteres."""

def contar_caracteres():
    texto_digitado = input('Digite um texto: ')
    
    print(f'A quantidade de caracteres é: {len(texto_digitado)}')
    
contar_caracteres()