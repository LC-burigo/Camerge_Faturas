import pandas

lista_andre = ['Consumidor 1']
lista_paulo = ['Consumidor 2']
lista_felipe = ['Consumidor 3']

dicionario_andre = {'Consumidor 1': 'PREMDGENTR101 (L)'}
dicionario_paulo = {'Consumidor 2': 'SCEMDGENTR101 (L)'}
dicionario_felipe = {'Consumidor 3': 'SPEMDGENTR101 (L)'}


def envio_medicoes(data, pessoa):
    if pessoa == 'andre':
        for agente in lista_andre:
            planilha_resumo = pandas.ExcelFile('C:/Users/burig/OneDrive/Documentos/Resumo {}.xlsx'.format(data))
            df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
            df = df[df['Ponto / Grupo'] == dicionario_andre[agente]]
            df = df.dropna()
            # df = df()
            # df = df['Ativa C (kWh)']
            df.to_excel('C:/Users/burig/OneDrive/Documentos/Resumo {}.xlsx'.format(agente))
    if pessoa == 'paulo':
        for agente in lista_paulo:
            planilha_resumo = pandas.ExcelFile('C:/Users/burig/OneDrive/Documentos/Resumo {}.xlsx'.format(data))
            df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
            df = df[df['Ponto / Grupo'] == dicionario_paulo[agente]]
            df = df.dropna()
            # df = df()
            # df = df['Ativa C (kWh)']
            df.to_excel('C:/Users/burig/OneDrive/Documentos/Resumo {}.xlsx'.format(agente))
    if pessoa == 'felipe':
        for agente in lista_felipe:
            planilha_resumo = pandas.ExcelFile('C:/Users/burig/OneDrive/Documentos/Resumo {}.xlsx'.format(data))
            df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
            df = df[df['Ponto / Grupo'] == dicionario_felipe[agente]]
            df = df.dropna()
            # df = df()
            # df = df['Ativa C (kWh)']
            df.to_excel('C:/Users/burig/OneDrive/Documentos/Resumo {}.xlsx'.format(agente))


envio_medicoes("jan-22", 'andre')
envio_medicoes("jan-22", 'paulo')
envio_medicoes("jan-22", 'felipe')


