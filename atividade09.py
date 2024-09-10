#Crie um programa onde o usuário cadastre uma quantidade desejada de eventos (nome do evento e classificação indicativa) e após o cadastro dos eventos, o usuário possa informar o nome e a idade, e se inscrever em um dos eventos. Caso o usuário não tenha idade mínima, o programa proíbe a inscrição e pede para o mesmo se inscrever em outro evento. Caso o usuário tenha a idade mínima, o programa inscreve o usuário exibindo a data da inscrição e encerra

#bliblioteca
import os
from datetime import date

#dicionario
eventos = []

dia = date.today().day
mes = date.today().month
ano = date.todat().year

while True:
    opcao = input('1 - para contratar evento. 2 - para se inscrever')
    os.system('cls')
    match opcao:
        case '1':
            evento = {}
            try:
                evento['nome'] = input('Ifore o evento: ')
                evento['censura'] = int(input('Informe a classificacao indicativa'))
                evento.append(evento)
                print('Evento cadastrado com sucesso!.')
            except Exception as e:
                print(f'Não foi possivel cadastrar evento {e}.') #este é tras a mensagem de erro do exception
            finally:
                continue
            case '2':
                nome = input('Informe o seu nome: ')
                idade = int(input('Informe a sua idade: '))
                while True:
                    print(f'\n{'-'*30}EVENTO{'-'*30}\n')
                    for i in range(len(eventos)):
                        print(f"Cód do evento: {i}")
                        for campo in eventos[i]:
                            print(f'{campo.capitalize()} : {evento[i].get(campo)}.')
                            print('-'*30)
                        try:
                            codigo_evento = int(input('Informe o cód do evento: '))
                            if codigo_evento >= 0 and codigo_evento <= len(eventos) : if idade >= eventos[codigo_evento].get('censura'):
                            print(f'{nome} foi inscrito no evento. Data da incrição: {dia}/{mes}/{ano}')
                            break
                            else:
                            print(f'{nome} não possui idade para inscrição. Volte ao menu.')
                            continue
                            else:
                            rint('cod do evento invalido.')
                            continue
                        except Exception as e:
                        print(f'Não foi possivel se inscrever para evento {e}.')
                        break
        break
    case_:
        print(f'Opcao Invalida.')
        break
