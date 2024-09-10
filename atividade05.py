#Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa
#um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.
#Import de Biblioteca
import os

#Lista
nomes = ['Adriano', 'Francisco', 'Eduardo', 'Moises', 'Maria', 'Joana','Amelia','Tereza','Mercedes','Tadeu','Jairo']

#Exibe alista ao usuario com seus respectivos indices
for i in range(len(nomes)):
    print(f'Indice {i} : {nomes[i]}.')

#Usuario informa qual o indice deseja ver
print('__________________________')
indice = int(input('Informe o numero do indice: '))
os.system('cls')

#retorna o nome digitado pelo usuario
if indice in nomes:
    print(f'O nome selecionado foi: [{nomes[indice]}]')
else:
    print('Não localizado!\n\n\n')

#--------------------------------------------------------------------------------------
#nomes ['nomes informados pelo usuario']
 #try:
#indice = int(input('informe o indice:'))

#print(nomes[indice] if indice >= 0 and indice < 10 else 'indice inexistente.')
#except Exception as e:
#print('bla,bla,bla')


