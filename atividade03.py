#Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.

#Importacao de biblioteca
import os

#Imput de dados
numero = int(input('Informe um numero Inteiro: '))
os.system('cls')#limpa o console


if numero % 2 == 0:
    print(f'O numero [{numero}] é um número PAR.\n')
else:
    print(f'O numero [{numero}] é um número IMPAR.\n')



