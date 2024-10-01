#Nível Python 2

# Cálculo de Consumo de Combustível

# Escreva um programa que ajude um motorista a calcular o consumo de combustível de seu veículo.
# O programa deve solicitar ao usuário que insira a distância percorrida e a quantidade de combustível consumido em várias viagens.
# Essas informações devem ser armazenadas em uma lista.
# Em seguida, crie uma função que percorra essa lista e calcule o consumo médio de combustível (km/l) para cada viagem e para o total de todas as viagens.

def calcular_consumo(distancia, combustivel):  #calcula o consumo médio de combustivel por viagem
    
    if combustivel == 0:  #se combustivel e == 0
        return "Divisão por zero! Verifique dos dados de entrada."
    else:  #outro
        return distancia / combustivel
    
def main():
    viagens = []  #lista
    while True:
        #Inserir dados do Usuario -- solicita ao usuário a distância e o consumo, validando os valores.
        distancia = float(input("Digite a distância percorrida (km): "))
        combustivel = float(input("Digite a quantidade de combustível consumido (L): "))
        if distancia <= 0 or combustivel <= 0:
            print("Valores invalidos. A distancia e o consumo devm ser positivos. ")
            continue

        viagens.append((distancia, combustivel)) #puxou os argumentos do inicio do codigo

        continuar = input("Deseja adicionar mais uma viagem? (s/n): ")
        if continuar.lower() != "s":
            break

    consumo_total = 0
    for distancia, combustivel in viagens:
        consumo = calcular_consumo(distancia, combustivel)
        print(f"Consumo médio da viagem: {consumo:.2f} km/l")
        consumo_total += consumo

    numero_viagens = len(viagens)
    if numero_viagens > 0:
        consumo_medio_total = consumo_total / numero_viagens
        print(f"Consumo médio total: {consumo_medio_total:.2f} km/l")
    else:
        print("Nenhuma viagem registrada.")

if __name__ == "__main__":
    main()