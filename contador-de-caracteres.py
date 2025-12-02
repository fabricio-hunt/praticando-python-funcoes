"""Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém."""

def contador():
    contador_de_vogais = input("Escreva um texto qualquer: ")
    cont = 0
    for letra in contador_de_vogais:
        if letra.lower() in 'aeiou':
            cont += 1
    print(f"O texto contém {cont} vogais.")  

contador()                     

