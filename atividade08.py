# Crie um programa em que o usuário informe uma quantidade desejada de números decimais de,
#  no mínimo 0 e no máximo 10, e o programa calcula a média desses números. (except Except as e)

#Lista de numeros
numerosDecimais = []

#input de dados do usuario
numero = int(input('\n\nInforme os numeros decimais entre minímo 0 e máximo 10: '))

#estrutura de decisao que valida se aquantidade corresponde ao determinado
if 0 >= numero:
    for i in range(numero):#se for True executa o comando para informar
        decimal = float(input(f'Informe o {i+1}ª numero: '))
        numerosDecimais.append(decimal)#armazena o numero no vetor

        #calculo da media
        media = sum(numerosDecimais) / len(numerosDecimais)

        #exibicao do resultado
        print(f'O resultado da média é: {media}')

elif numero <= 10:
    for i in range(numero):#se for True executa o comando para informar
        decimal = float(input(f'Informe o {i+1}ª numero: '))
        numerosDecimais.append(decimal)#armazena o numero no vetor

        #calculo da media
        media = sum(numerosDecimais) / len(numerosDecimais)

        #exibicao do resultado
        print(f'O resultado da média é: {media}')


else:
    print('Quantidade Invalida. Programa encerrado!\n\n')

#_________________________outro modo_______________________________
# import os
# notas = []
# while True;
# opcoes = input(' 1 inserir ou 2 calcular media')
# os.system('cls')
# match opcao:
#   case '1':
#       try:
#          novaNoata = float(input(Informe a nota 0 a 10: ));repalce(',','.')
#          if novaNota >= 0 and novaNota <= 10:
#               notas.append(novaNota)
#               print('Inserido com sucesso')
#          else:
#               print('invalido')
#       except Exception as e:
#               print('nao possivel inserir')
#       finally:
#           continue
#       case '2':
#           break
#       case _:
#           print('opcao invalida')
#            continue
#print(f'media: {sum(notas)/len(notas)):,.2f}')

