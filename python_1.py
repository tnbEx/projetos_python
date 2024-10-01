#Nível Python 1

#Simulador de investimentos

# Crie um programa que simule o crescimento de um investimento ao longo de um período.
# O programa deve solicitar ao usuário o valor inicial do investimento, a taxa de juros anual e o número de anos.
# Em seguida, escreva uma função que calcule o valor final do investimento ao final de cada ano e armazene esses valores em uma lista.
# Imprima o valor acumulado ano a ano (lembre-se que se trata de juros compostos)

def simulador_investimento(valor_inicial, taxa_juros, anos):  #Simula o crescimento de um investimento ao longo dos anos
    
    #Args:
    #valor_inicial: valor investimento inicial
    #taxa_juros: A taxa de juros anual em decimal (ex:1-% = 0.1)
    #anos: numero de anos da simulação

    #Returns:
    valores_acumulados = []  #Uma lista com os valores acumulados ao final de cada ano.
    valor_atual = valor_inicial #variavel puxa argumentos Loop For
    for ano in range(1, anos + 1):
        valor_atual *= (1 + taxa_juros)
        valores_acumulados.append(valor_atual)

    return valores_acumulados

#Obtendo dados do Usuário
valor_inicial = float(input("Digite o valor inicial do investimento: ")) 
taxa_juros = float(input("Digite a taxa de jurtos anual (em decimal): "))
anos = int(input("Digite o número de anos: "))

#Chamando a Função e imprimindo resultados
resultado = simulador_investimento(valor_inicial, taxa_juros, anos)

for ano, valor in enumerate(resultado, start=1):
    print(f"Após {ano} ano(s), o valor acumulado é: R$ {valor:.2f} ")