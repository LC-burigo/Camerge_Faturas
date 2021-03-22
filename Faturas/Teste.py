import pandas
import openpyxl

excel_file = pandas.read_excel("C:/Users/burig/OneDrive/Documentos/Disciplina de comercialização/ANEEL BIG.xlsx", engine='openpyxl')
print(excel_file.info())

