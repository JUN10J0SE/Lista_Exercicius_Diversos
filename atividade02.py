#Crie um programa que receba o peso (em gramas) de um bebê recém-nascido
#e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.
# ? (peso >= 2500) "bebe ok" : "bebe doente"; -operador ternario em Java-

#Importacao da Biblioteca
import os

#Imput de dados 
peso = str(input('Informe o peso do Bebé em gramas: ')).replace(',','.')
os.system('cls')#Limpa o console

peso = float(peso)

if peso >= 2500:
    print('O bebé está saudavel, parabéns!\n\n')
else:
    print(f'O bebe esta abaixo do peso, procure ajuda médica! [{peso}g]')