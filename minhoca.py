#Minhoquinha 1
#Receber String
def criar_lista_de_string(string):
    lista_de_caracteres = []

#Criar Loop For
    for caractere in string: 
        lista_de_caracteres.append(caractere)
    return lista_de_caracteres

#Entrada Usuario
string_usuario = input("Digite uma string: ")

#Chamar função
lista_final = criar_lista_de_string(string_usuario)
print("A lista de caracteres é: ", lista_final)

#______________________________________________

#Minhoquinha 2


numeros = [] #Lista armazenar

#Criar loop  while e inserir numeros "usuario"
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break

print("A lista de números é: ", numeros)

#______________________________________________

#Minhoquinha 3

def calcular_media(lista_numeros):

    soma = 0
#Usando for para calcular a media
    for numero in lista_numeros:
        soma += numero
    
    media = soma / len(lista_numeros)
    return media

#Uso
minha_lista = [1, 2, 3, 4, 5, 6]
resultado = calcular_media(minha_lista)
print("A média dos números é: ", resultado)

#______________________________________________

#Minhoquinha 4

def imprime_mensagem(mensagem):
   "Eu vou aprender essa bagaça"
   print(mensagem)
   return;

imprime_mensagem( mensagem = "Eu vou aprender")

#______________________________________________

#Minhoquinha 5

def saudacao(nome):
    "Olá, Ruan! "
    print("Olá", format(nome))
    return

saudacao("TNB")
saudacao("Eu sou o optimus prime")

#______________________________________________

#Minhoquinha 6

def saudacao(nome="Usuario"):
    "Olá, Ruan! "
    print("Olá", format(nome))
    return

saudacao()
saudacao("TNB")
saudacao("Eu sou o optimus prime")



