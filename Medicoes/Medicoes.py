from lib2to3.pgen2.pgen import DFAState
import pandas
import os

lista_andre = ['Copaza', 'Ecofrigo CL', 'Jurerê Beach Village', 'Máquinas Omil', 'MDG Filmes', 'Seara Filial Itajai CL']

lista_paulo = ['AB Plast', 'Althoff', 'ALUMASA', 'Alump', 'Catarinense Pharma', 'COOPER', 'Cordoaria', 'Cristalpombos','Cristalsul', 'Estilo Madeiras', 'Gaboardi', 'Habitasul', 'Hippo', 
               'Ibraflex', 'Imperatriz', 'Moinho_Catarinense', 'Móveis_Daico', 'Nutriforte', 'Nutrisul', 'PEF_Supermercados', 'Primo Tedesco Canoas','Primo Tedesco Papel','Primo Tedesco Sacos','Retail_Park', 'Rumobrás', 'Sefar', 'Temasa CL', 'Textilfio', 'Vipel'
               ]

lista_felipe = ['CLL GROUP', 'Ecofrigo CL', 'LATICINIOS OLIVEIRA', 'MATISA', 'MINAPLAST CL', 'PÁTIO CHAPECÓ', 'SUPERMERCADOS SCHUTZE', 'TORRECID SC', 'TORRECID SP', 'UNESC', 'UNIPEÇAS']

lista_george = ['Althoff', 'Artely Moveis', 'Brasnile', 'Fios Bem Brasil', 'Flexibag', 'Ibrap SP', 'Riva', 'Somapar', 'Sr.Pão', 'UCEFF']

lista_davi = ['5 Plastic', 'Alumetaf CL', 'Alump', 'Conexão Marítima', 'Copaza', 'Imam 2', 'Imam', 'Jurerê Beach Village', 'SBM', 'Vipel']

dicionario_andre = {'Copaza': 'SCCPIRENTR101 (L)', 'Ecofrigo CL': 'SCEFGCENTR101 (L)', 'Jurerê Beach Village': 'SCJBVJENTR101 (L)', 'Máquinas Omil': 'SCOMIBENTR101 (L)', 'MDG Filmes': 'AMMDMOENTR101 (L)', 
                    'Seara Filial Itajai CL': 'SCSFITENTR101 (L)'}

dicionario_paulo = {'AB Plast': 'SCABPJENTR101 (L)', 'Althoff': ['SCALTIENTR101 (L)', 'SCALTCENTR101 (L)', 'SCALURENTR101 (L)', 'SCALTGENTR101 (L)', 'SCALORENTR101 (L)', 'SCALTHENTR101 (L)', 'SCALTTENTR101 (L)','SCALCNENTR101 (L)'],
                    'ALUMASA': 'SCALMSENTR101 (L)', 'Alump': 'SCALTBENTR101 (L)', 'Catarinense Pharma': 'SCLCTJENTR101 (L)', 
                    'COOPER': ['SCCOOVENTR101 (L)', 'SCCPGBENTR101 (L)', 'SCCPDGENTR101 (L)', 'SCCPIAENTR101 (L)', 'SCCPCIENTR101 (L)', 'SCCPNIENTR101 (L)','SCCPWIENTR101 (L)','SCVIJBENTR101 (L)','SCCPJRENTR101 (L)','SCVIJNENTR101 (L)','SCCPNBENTR101 (L)',
                    'SCCVIBENTR101 (L)','SCCPVBENTR101 (L)','SCCCVIENTR101 (L)','SCCPTMENTR101 (L)','SCCPROENTR101 (L)'], 
                    'Cordoaria': 'SCCOBIENTR101 (L)', 'Cristalpombos': 'PECTOBENTR101 (L)','Cristalsul': 'SCCTSIENTR101 (L)', 'Estilo Madeiras': 'PREMDGENTR101 (L)', 'Gaboardi': ['SCFFGBENTR101 (L)', 'SCFFBRENTR101 (L)'], 
                    'Habitasul': ['SCHBFLENTR101 (L)', 'SCHBSMENTR101 (L)'], 'Hippo': ['SCHPAFENTR101 (L)', 'SCHPCOENTR101 (L)', 'SCHPLMENTR101 (L)', 'SCHPUNENTR101 (L)'], 'Ibraflex': 'SCIXCHENTR101 (L)',
                    'Imperatriz': ['SCIZSAENTR101 (L)', 'SCIZAZENTR101 (L)', 'SCIZ03ENTR101 (L)', 'SCIZCBENTR101 (L)', 'SCIZAPALIMP01 (L)', 'SCIZDEENTR101 (L)','SCIZ08ENTR101 (L)','SCIZIFENTR101 (L)', 'SCIPZCENTR101 (L)','SCIZJBENTR101 (L)',
                    'SCIZ16ENTR101 (L)', 'SCIZMRENTR101 (L)','SCIZARENTR101 (L)','SCIZBCALIPZ01 (L)','SCIZ22ENTR101 (L)','SCIZSGENTR101 (L)','SCIZSSENTR101 (L)','SCIZ23ENTR101 (L)','SCIZSIENTR101 (L)','SCIZRSENTR101 (L)','SCIZTDENTR-01 (L)','SCIZPLENTR101 (L)','SCIZJEENTR101 (L)','SCIZIJENTR101 (L)'], 
                    'Moinho_Catarinense': ['SCMCMFENTR101 (L)', 'SCMCM2ENTR101 (L)'], 'Móveis_Daico': ['SCMODBENTR101 (L)','SCMODIENTR101 (L)'], 'Nutriforte': 'SCNFSDENTR101 (L)', 'Nutrisul': ['SCNSLPENTR101 (L)', 'SCNUSLENTR101 (L)'], 
                    'PEF_Supermercados': ['SCPGLLENTR101 (L)','SCPGGAENTR101 (L)','SCPGSUENTR101 (L)','SCPGARENTR101 (L)','SCPSPVENTR-01 (L)'], 'Primo Tedesco Canoas': 'RSPTCNENTR101 (L)', 'Primo Tedesco Papel':'SCPTDCENTR101 (L)', 
                    'Primo Tedesco Sacos' : 'SCPTDPENTR101 (L)', 'Retail_Park' : ['SCRPPLENTR101 (L)','SCRPPBENTR101 (L)'], 'Rumobrás': 'SCTSCCENTR101 (L)', 'Sefar': 'RSSFPBENTR101 (L)', 'Temasa CL': 'SCTMM-ENTR101 (L)', 'Textilfio': ['SCTFGMENTR101 (L)', 'SCTFJGENTR101 (L)'], 'Vipel': 'SCVPTUENTR101 (L)'}

dicionario_felipe = {'CLL GROUP': 'SCCGIRENTR101 (L)', 'Ecofrigo CL': 'SCEFGCENTR101 (L)', 'LATICINIOS OLIVEIRA': 'SCLOVGENTR101 (L)', 'MATISA': 'SCMTCCENTR101 (L)', 'MINAPLAST CL': 'SCMPLTENTR-01 (L)', 'PÁTIO CHAPECÓ': 'SCSHCHALCON01 (L)', 
                     'SUPERMERCADOS SCHUTZE': 'SCSSHTENTR101 (L)', 'TORRECID SC': 'SCTRCIENTR101 (L)', 'TORRECID SP': 'SPTRARENTR101 (L)', 'UNESC': 'SCUNCRENTR101 (L)', 'UNIPEÇAS': 'SCUPCRENTR101 (L)'}

dicionario_george = {'Althoff': ['SCALTIENTR101 (L)', 'SCALTCENTR101 (L)', 'SCALURENTR101 (L)', 'SCALTGENTR101 (L)', 'SCALORENTR101 (L)', 'SCALTHENTR101 (L)', 'SCALTTENTR101 (L)','SCALCNENTR101 (L)'],
                     'Artely Moveis': 'PRASJPENTR101 (L)', 'Brasnile': ['SCBNTBENTR101 (L)', 'SCBNTBENTR101 (L)'], 'Fios Bem Brasil': 'SCFIBBENTR101 (L)', 'Flexibag': 'PRFBGCENTR101 (L)', 'Ibrap SP': 'SPIBSOENTR101 (L)', 'Riva': 'SCRVFBENTR101 (L)', 'Somapar': 'PRSPUVENTR101 (L)', 'Sr.Pão': 'SCSRJSENTR101 (L)', 'UCEFF': 'SCUCITENTR101 (L)'}

dicionario_davi = {'5 Plastic': 'SC5PSCENTR101 (L)', 'Alumasa CL': 'SCALMSENTR101 (L)', 'Alumetaf CL': 'SCFATFENTR101 (L)', 'Alump': 'SCALTBENTR101 (L)', 'Conexão Marítima': 'SCCMIJENTR101 (L)', 'Copaza': 'SCCPIRENTR101 (L)', 'Imam 2': 'SCMTRUENTR101 (L)', 'Imam': 'SCMTRUENTR101 (L)', 'Jurerê Beach Village': 'SCJBVJENTR101 (L)', 'MATISA': 'SCMTCCENTR101 (L)', 'OESA SC': 'SCOEJSENTR101 (L)', 
                   'SBM': ['SCSBMSENTR101 (L)', 'SCSBMVENTR101 (L)', 'SCSBMMENTR101 (L)', 'SCSBMFENTR101 (L)', 'SCSBMLENTR101 (L)'], 'Vipel': 'SCVPTUENTR101 (L)'}

def envio_medicoes(data, pessoa):
    if pessoa == 'andre':
        for agente in lista_andre:
            if os.path.isfile('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/André/{}/{}.xlsx'.format(data, agente)):
                print('A planilha {}.xlsx já existe'.format(agente))
            else:   
                planilha_resumo = pandas.ExcelFile('//192.168.0.2/Perfis/lucas.burigo/Desktop/Resumo {} teste.xlsx'.format(data))
                df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
                df = df[df['Ponto / Grupo'] == dicionario_andre[agente]]
                df = df.dropna()
                df.to_excel('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/André/{}/{}.xlsx'.format(data, agente))
    if pessoa == 'davi':
        for agente in lista_davi:
            if os.path.isfile('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/Davi/{}/{}.xlsx'.format(data, agente)):
                print('A planilha {}.xlsx já existe'.format(agente))
            else:   
                planilha_resumo = pandas.ExcelFile('//192.168.0.2/Perfis/lucas.burigo/Desktop/Resumo {} teste.xlsx'.format(data))
                df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
                if agente == 'SBM':
                    df = SBM(df, agente)
                else:
                    df = df[df['Ponto / Grupo'] == dicionario_davi[agente]]
                    df = df.dropna()
                df.to_excel('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/Davi/{}/{}.xlsx'.format(data, agente))
    if pessoa == 'george':
        for agente in lista_george:
            if os.path.isfile('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/George/{}/{}.xlsx'.format(data, agente)):
                print('A planilha {}.xlsx já existe'.format(agente))
            else:   
                planilha_resumo = pandas.ExcelFile('//192.168.0.2/Perfis/lucas.burigo/Desktop/Resumo {} teste.xlsx'.format(data))
                df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
                if agente == 'Althoff':
                    df = Althoff(df, agente)
                elif agente == 'Brasnile':
                    df = Brasnile(df, agente)
                else:
                    df = df[df['Ponto / Grupo'] == dicionario_george[agente]]
                    df = df.dropna()
                df.to_excel('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/George/{}/{}.xlsx'.format(data, agente)) 
    if pessoa == 'paulo':
        for agente in lista_paulo:
            if os.path.isfile('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/Paulo/{}/{}.xlsx'.format(data, agente)):
                print('A planilha {}.xlsx já existe'.format(agente))
            else:
                planilha_resumo = pandas.ExcelFile('//192.168.0.2/Perfis/lucas.burigo/Desktop/Resumo {} teste.xlsx'.format(data))
                df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
                if agente == 'Althoff':
                    df = Althoff(df, agente)
                elif agente == 'COOPER':
                    df = COOPER(df, agente)
                elif agente == 'Gaboardi':
                    df = Gaboardi(df, agente)
                elif agente == 'Habitasul':
                    df = Habitasul(df, agente)
                elif agente == 'Hippo':
                    df = Hippo(df, agente)
                elif agente == 'Imperatriz':
                    df = Imperatriz(df, agente)
                elif agente == 'Moinho_Catarinense':
                    df = Moinho_Catarinense(df, agente)
                elif agente == 'Móveis_Daico':
                    df = Móveis_Daico(df, agente)
                elif agente == 'Nutrisul':
                    df = Nutrisul(df, agente)
                elif agente == 'PEF_Supermercados':
                    df = PEF_Supermercados(df, agente)
                elif agente == 'Retail_Park':
                    df = Retail_Park(df, agente)
                elif agente == 'Textilfio':
                    df = Textilfio(df, agente)
                else:
                    df = df[df['Ponto / Grupo'] == dicionario_paulo[agente]]
                    df = df.dropna()
                df.to_excel('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/Paulo/{}/{}.xlsx'.format(data, agente))
    if pessoa == 'felipe':
        for agente in lista_felipe:
            if os.path.isfile('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/Felipe/{}/{}.xlsx'.format(data, agente)):
                print('A planilha {}.xlsx já existe'.format(agente))
            else:
                planilha_resumo = pandas.ExcelFile('//192.168.0.2/Perfis/lucas.burigo/Desktop/Resumo {} teste.xlsx'.format(data))
                df = pandas.read_excel(planilha_resumo, header=3, index_col=0)
                df = df[df['Ponto / Grupo'] == dicionario_felipe[agente]]
                df = df.dropna()
                df.to_excel('S:/Tecnico/Controle de Atividades - Camerge/Controle de Atividades - Gerência André/BACK/Enviar medições para Cálculo da FLEX/Felipe/{}/{}.xlsx'.format(data, agente))


def Althoff(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][2]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][3]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][4]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][5]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][6]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][7])]
    df = df.dropna()
    return df

def COOPER(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][2]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][3]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][4]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][5]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][6]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][7]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][8]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][9]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][10]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][11]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][12]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][13]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][14]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][15])]
    df = df.dropna()
    return df

def Gaboardi(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def Habitasul(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def Hippo(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][2]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][3])]
    df = df.dropna()
    return df 

def Imperatriz(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][2]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][3]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][4]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][5]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][6]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][7]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][8]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][9]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][10]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][11]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][12]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][13]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][14]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][15]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][16]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][17]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][18]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][19]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][20]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][21]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][22]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][23])]
    df = df.dropna()
    return df    

def Moinho_Catarinense(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def Móveis_Daico(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def Nutrisul(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def PEF_Supermercados(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][2]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][3]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][4])]
    df = df.dropna()
    return df

def Retail_Park(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def Textilfio(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_paulo[agente][0]) | (df['Ponto / Grupo'] == dicionario_paulo[agente][1])]
    df = df.dropna()
    return df

def Brasnile(df, agente):
     df = df[(df['Ponto / Grupo'] == dicionario_george[agente][0]) | (df['Ponto / Grupo'] == dicionario_george[agente][1])]
     df = df.dropna()
     return df

def SBM(df, agente):
    df = df[(df['Ponto / Grupo'] == dicionario_davi[agente][0]) | (df['Ponto / Grupo'] == dicionario_davi[agente][1]) | (df['Ponto / Grupo'] == dicionario_davi[agente][2]) | (df['Ponto / Grupo'] == dicionario_davi[agente][3]) | (df['Ponto / Grupo'] == dicionario_davi[agente][4])]
    df = df.dropna()
    return df

#envio_medicoes("fev-22", 'andre')
#envio_medicoes("jan-22", 'paulo')
#envio_medicoes("jan-22", 'felipe')
#envio_medicoes("jan-22", 'george')
#envio_medicoes("jan-22", 'davi')
