#Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva.

#Importacao de biblioteca
import os
import time

#Imputacao de dados
numero = int(input('Informe um numero: '))

while numero >= 0:
    os.system('cls')
    print(f'Contagem regressiva.... {numero}')
    
    numero -= 1
    time.sleep(3)

os.system('cls')
print('Bummmmm')

#usando com o for
#for  i in range(numero, -1, -1): o primeiro -1 é onde estoura e o 2ª a quantedade que subtraia se -1 ou -2 e etcc...
#print(f'{i}...')
#time.sleep(1)
#os.system('cls')
