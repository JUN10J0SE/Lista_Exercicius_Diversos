# Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.

#Importacao de biblioteca OS para evocar o limpador de console
import os

#Lista
nomes = []

#Loop de menu que forca o usuario a escolher a opcao
while True:
    #opcoes de menu mostrada ao usuario
    print('\n\n')
    print('[1] - Inserir nome:')
    print('[2] - Exibir total de nomes:')
    print('[3] - sair:')

    #informa o menu
    opcao = int(input('Informe a opção desejada: '))

    os.system('cls') #limpador

    #execucao do menu
    match opcao:
        case 1:
            novo_nome = str(input('Informe o nome: '))
            nomes.append(novo_nome)#grava o nome na Lista
            nomes.sort()#ordena pela ordem alfabedica a exibicao da lista
            os.system('cls')

            print('--------------------------------------------------')
            print(f'O nome [{novo_nome}] foi aramazenado com sucesso.')#exibe ao usuario o nome que foi armazenado
            print('--------------------------------------------------')
            
            for i in range(len(nomes)):
                print(f'O nome armazenado na posição [{i}] é:  {nomes[i]}')#exibe ao usuario o nome armazenado e seu indice
                continue

        case 2:
            print(f'Total de nomes armazenados na lista: {len(nomes)}')#informa o total de nomes armazenados
            print('__________________________________________________')
            continue

        case 3:
            print('________________________')#mostra a mensagem de armazenamento
            print('___PROGRAMA ENCERRADO___')
            print('________________________\n\n')
            break
        case _:
            print('Opção Invalida! - Tente novamente')#caso digite um numero que nao esteja no menu
            print('_________________________________\n\n')

#__________________________outro modo_______________________________________
# import os
# nomes = []
# while True:
# novoNome = input('Informe os nomes ou deixe em branco para encerrar')
# os.system('cls')
# if novoNome != '':
#   try:
#       nomes.append(novoNome)
#       print(f'{novoNome} inserido.')
#   except Exception as e:
#       print('Noa foi possivel inserrir')
#   finaly:
#       continue - o finele nao deixa o programa encerrar mesmo se for para o except. ele retorna ao menu mesmo com erro informado -
# else:
#   brack
# nomes.sort()
# print(f'numero de nomes na lista: {len(nomes)}.')
# for nome in nomes:
#   print(nome) 
