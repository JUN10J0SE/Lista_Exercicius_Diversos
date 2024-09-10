#Crie um programa que traduza qualquer texto em qualquer idioma para o português.

from deep_translator import GoogleTraslator #precisa pipi nstal

tradutor = GoogleTraslator(source = 'auto', target = 'pt')

while True:
    try:
        texto_original = input('Digite o texyo a ser traduzido para pt ou Enter encerrar')
        if texto_original != '':
            texto_original = tradutor.translate(texto_original)
            print(texto_original)
            continue
        else:
            break
    except Exception as e:
        print(' Erro ao traduzir {e}.')
        break