import os
import tabula

#pasta = '/media/vinicio/programas/projetos/estudos/convert-pdf-to-excel/pdfs'
pasta = input('Digite o caminha da pasta onde estão os PDF`s: ')

caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
pdfs = [arq for arq in arquivos if arq.lower().endswith(".pdf")]

print('Todos os arquivos PDF`s no diretorio', pdfs)

for arquivo in pdfs:
    print('PDF => ', arquivo)
    tabula.convert_into(f'{arquivo}', f'{arquivo.replace(".pdf", ".csv")}', output_format='csv', pages='all')
    print('Convertido para => ', arquivo.replace(".pdf", ".csv"))

print('Fim do programa!')

















