def calculando_idade():
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano atual: : '))
    
    calculando_idade = (ano_atual - ano_nascimento)
    print(f"Sua idade é {calculando_idade}")
    
calculando_idade()
    

   #resposta instrutor(a)

"""
    def calcular_idade(ano_nascimento, ano_atual): 
        return ano_atual - ano_nascimento 
    
    nascimento = int(input("Digite o ano de nascimento: ")) 
    atual = int(input("Digite o ano atual: ")) 
    idade = calcular_idade(nascimento, atual) 
    print(f"A idade é {idade} anos.") 

"""