# import PyPDF2
# import json
#
# object = open(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\BRUNETTA_MEGA WATT.pdf', 'rb')
# reader = PyPDF2.PdfFileReader(object)
# page = reader.getPage(0)
# page_content = page.extractText()
# data = json.dumps(page_content)
# formatj = json.loads(data)
# print(data)

from tabula import read_pdf
import re

df = read_pdf(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\BRUNETTA_MEGA WATT.pdf', pages=1, output_format="json")
print(df[0])
print(df[1])
print(df[2])
print(df[3])
print(df[4])
print(df[5])
print(df[6])
print("extraction_method: {}".format(df[0]['extraction_method']))



