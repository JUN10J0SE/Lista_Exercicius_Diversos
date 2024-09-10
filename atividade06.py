#Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos (divisivel por 1 e por ele mesmo).

#Funcao para verificar numeros primos
def primos(numeros):
    if numeros < 2:
        return False
    
    for i in range(2, int(numeros ** 0.5)+1):
        if numeros % i == 0:
            return False
    
    #Retorna o valor dos numeros primos
    return True 

#lista de aramazenamento dos numeros
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#arrey vazio armazenar numeros primos quando for chamada
guardarPrimo = []

for numero in num:
    if primos(numero):
        guardarPrimo.append(numero)

#print de demostracao dos numeros primos
print(f'Os numeros primos de 1 a 20 são: {guardarPrimo}')

#---------------------------outro modo--------------------------------------------------
# import math
# def primos(numero):
#   if numero < 2:
#       return False
#   else:
#        ....
#   for i in range(2, int(math.sqrt(numero)) + 1):
#       if numero % i ==0:
#           return false
#       else:
#           ....
#   return True
# if _neme__ == '__main__':
# numero = ['dados informados e etc...]
#
# print('Lista dos numeros primos')
# for numero in numeros:
# if primo(numero):
#   print(f'o numero {numero} é primo')
# else:
#   ....   


        



