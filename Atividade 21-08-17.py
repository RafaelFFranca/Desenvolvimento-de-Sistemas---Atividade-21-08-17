"""Rafael Fernandes França - RA: 1700791
   Rilmo Ponciano - RA: 1700143
   Henrique Cardoso - RA: 1601600"""

#Exercício 1

print("Exercicio 1")

def troca(vetor):
    for i in range(30):
        if vetor[i] >= 1:
            vetor[i] = 1
        else:
            vetor[i] = 0
    return vetor

vet = [0]*30
for i in range (30):
    vet[i] = int(input("digite um valor: "))
    
print (vet)

troca(vet)

print (vet)

#Exercício 2

print("Exercicio 2")

def alteracao (lista):
    for i in range (5):
        if lista[i] < 0:
            lista[i] = 0
        elif lista[i] < 10:
            lista[i] = 1
        else:
            lista[i] = 2
    return lista

    
vet = [0]*5
for i in range (5):
    vet[i] = int(input (" Digite um número: "))

print (vet)

alteracao (vet)

print (vet)


#Exercício 3

print ("Exercicio 3")
n = int(input ("Digite um número: "))
if n < 0:
    print (n*-1)
elif n > 10:
    n2 = int(input("Digite outro nº: "))
    print (n-n2)
else:
    n3 = n/5
    print (n3)

#Exercício 4
print ("Exercicio 4")
arquivo = open ("novo_arquivo.txt" , "w")
for i in range (1):
    arquivo.write ("Estou cursando Banco de Dados!")
arquivo.close()

arquivo = open ("novo_arquivo.txt" , "r")
for linha in arquivo:
    print ("" , linha)
arquivo.close()

arquivo = open ("arquivo.txt" , "r")
copia_arq = open ("copia_arq.txt" , "w")
while 1:
    texto = arquivo.read(35)
    if texto == "":
        break
    copia_arq.write(texto)
arquivo.close()
copia_arq.close()

#Exercicio 5
print("Exercicio 5")
relatorio = open("relatorio.txt", "w")

import math

def soma(espaco):
    return sum(espaco)

def media(espaco):
    return float(sum(espaco))/len(espaco)

relatorio.write("ACME Inc.    Uso do espaço em disco pelos usuários\n")
relatorio.write("-"*50)
relatorio.write("\n Nr.   Usuário     Espaço Utilizado    % do Uso \n")
user = ["Alexandre" , "Anderson", "Antonio", "Carlos", "Cesar", "Rosemary"]
espaco = [434.99, 1187.99, 117.73, 87.03, 0.94, 752.88]
perc = [16.85, 46.02, 4.56, 3.37, 0.04, 29.16]

for i in range(6):
    relatorio.write('\n %i     %s       %4.2f MB      %4.2f %% \n' % (i+1 , user[i], espaco[i], perc[i]))

relatorio.write("\nEspaço total ocupado: %4.2f MB \n" %(soma(espaco)))
relatorio.write("Espaço médio ocupado: %4.2f MB \n" %(media(espaco)))

relatorio.close()


