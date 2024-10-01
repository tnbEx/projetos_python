#Cobrinha 1

def potencia(base, expoente=2):

    return base ** expoente

resultado1 = potencia(2,3)
print(resultado1)

resultado2 = potencia (5)
print(resultado2)

#_____________________________________________

#Cobrinha 2

def maior_valor(num1, num2, num3):
 
#Args
#ultilizando a função max - para encontrar o maior valor
    maior = max(num1, num2, num3)
    print(f"O maior valor é: {maior}")

    numeros = [num1, num2, num3]
    numeros.sort()

    return numeros

#chamando a funcao - return
resultado = maior_valor(5, 2, 8)
print(resultado)

#_____________________________________________

#Cobrinha 3

def imprime_dados(nome, preco, quantidade):  #Imprime os dados de um produto de forma organizada.
    
    #Args
    print(f"Produto: {nome}")
    print(f"Preco: R$ {preco:.2f}")
    print(f"Quantidade em estoque: {quantidade}")

#chamando a função - returns
imprime_dados(nome="Smartphone", preco=1599.99, quantidade=10)

#____________________________________________

#Cobrinha 4 - Docstring(python) 

#____________________________________________

#Cobrinha 5

def exibir_mensagem(mensagem, repeticoes=1):
    #Imprime uma mensagem um determinado número de vezes.

    #Args
    #mensagem ("Número de vezes especificado")
    #repeticoes("O número de vezes que a mensagem será impressa")

    for _ in range(repeticoes):
        print(mensagem)
    
#chamar funçao - return
exibir_mensagem("Olá mundo!", 4)
exibir_mensagem("Python e divertido!", 3)

#___________________________________________

#Cobrinha 6

def gerar_lista_pares(n):
    #Gera uma lista com todos os números pares de 0 até n.

    #Args:
    #n: O número limite até onde os pares serão gerados.

    #Returns:
    #Uma lista contendo os números pares de 0 até n.
  
    lista_pares = []
    for numero in range(0, n+1, 2):
        lista_pares.append(numero)
        return lista_pares

#Chama função
numero_limite = int(input("Digite um número: ")) #usuario inserir numero
lista_resultado = gerar_lista_pares(numero_limite) #defini variavel + pega função + dados do usuario
print(lista_resultado)