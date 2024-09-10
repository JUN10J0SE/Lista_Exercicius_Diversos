#10.  Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela

import os

cursos = {}

while True:
    opcao = input('Para cadastrar novo curso ou 2 para exibir a lista de cursos cadastradas: ')
    os.system('cls')
    match opcao:
        case '1':
            curso = ()
            try:
                curso['Nome'] = input('Informe o novo curso: ').capitalize()
                curso['Dutracao do curso'] = int(input('Informe a duracao do curso'))
                curso['curso periodo'] = input('Matututino, Vespertino, Noturno').lower()
                curso['vagas'] = int(input('Informe o numero d evagas: '))
                cursos.append(curso)
                print('Curso cadastrado com sucesso!')
            except Exception as e:
                print(f'Não foi posssivel cadastrar novo curso. {e}:')
            finally:
                continue
        case '2':
            for curso in cursos:
                for campo in curso:
                    print(f'{campo} : {curso.get(campo)}.')
                print('-'*30)
            break
        case _:
            print('Opxcao invalida')
            continue