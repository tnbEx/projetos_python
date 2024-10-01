#Nivel Python 3

#Monitoramento de Temperatura

# Escreva um programa que utilize um laço while para solicitar ao usuário que informe a hora do registro da temperatura (em um número inteiro) 
# seguido do valor da temperatura registrada. 
# Seu programa deverá conter função de validação da entrada do usuário para garantir que a hora descrita esteja entre 0h e 23h
# e que a temperatura informada esteja entre -15ºC e 60ºC. 
# E em seguida armazene as informações em duas listas, uma com os horários e outra com as temperaturas.

def validar_hora(hora): #Valida se a hora está entre 0 e 23
    return 0 <= hora <= 23 #True se a hora for valida, False caso contrario

def validar_temperatura(temperatura): #Valida se a temperatura esta entre -15 e 60
    return -15 <= temperatura <= 60  #True se a temperatura for valida, False caso contrario.


def calcular_media_ponderada(horas, temperaturas):  #Calcula a média ponderada das temperaturas, considerando o intervalo de tempo.
    
    med_pond = 0
    intemp = 0
    for i in range(1, len(horas)):
        intervalo = horas[i] - horas[i-1]
        media = intervalo
        med_pond += temperaturas[i] * media
        intemp += media
    if intemp == 0:
        return None  # Caso não haja variação nas horas
    return med_pond / intemp
    

def encontrar_extremos(temperaturas):  #Encontra a temperatura mais baixa e mais alta e seus respectivos horários
    min_temp = min(temperaturas)
    max_temp = max(temperaturas)
    return min_temp, max_temp

#Listas para armazenar os dados
horas = []
temperaturas = []

while True:  #solicitar os dados ao usuário.
        entrada = input("Digite a hora (0-23) e a temperatura (-15 a 60), separadas por espaço, ou 'Fim' para encerrar: ")
        if entrada.lower() == 'fim':
            break

        try:
            hora, temperatura = map(float, entrada.split())
            if not validar_hora(hora):
                print("Hora inválida. Digite um valor entre 0 e 23.")
                continue
            if not validar_temperatura(temperatura):
                print("Temperatura inválida. Digite um valor entre -15 e 60.")
                continue
            horas.append(hora)
            temperaturas.append(temperatura)
        except ValueError:
            print("Entrada inválida. Por favor, digite a hora e a temperatura corretamente.")


#Calculando a media ponderada e os extremos
media = calcular_media_ponderada(horas, temperaturas)
min_temp, max_temp = encontrar_extremos(temperaturas)

#imprimindo resultados
if media is None:
    print("Não foi possível calcular a média devido à falta de variação nas horas.")
else:
    print(f"A média ponderada das temperaturas é: {media:.2f}°C")
    print(f"A temperatura mínima registrada foi: {min_temp}°C")
    print(f"A temperatura máxima registrada foi: {max_temp}°C")

    if 20 <= media <= 30:
        print("A temperatura média está dentro do intervalo de segurança.")
    else:
        print("A temperatura média está fora do intervalo de segurança.")