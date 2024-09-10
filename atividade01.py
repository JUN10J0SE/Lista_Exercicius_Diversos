#Crie um programa que peça para que o usuário digite um número, em seguida o converta para float
#exibindo em tela tanto o número em si quanto seu tipo de dado.

#insercao de dados
numero = int(input('Informe um Numero Inteiro: '))

#Conversao de inteiro para float
numero = float(numero)

#Print da tela
print(f'O seu numero digitado é: {numero} [',type(numero),']')# Comando type informa o tipo de dado

