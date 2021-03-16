from Faturas.Baixar_Faturas import main
from Faturas.Mudar_caminho import change_path
import os


def salvar_faturas():
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\{}'.format("marilda.pdf")):
        print("The {} file already exists".format("marilda.pdf"))
    else:
        main("01/2021")

        change_path("marilda.pdf")
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\{}'.format("marilda2.pdf")):
        print("The {} file already exists".format("marilda2.pdf"))
    else:
        main("02/2021")
        change_path("marilda2.pdf")
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\{}'.format("marilda3.pdf")):
        print("The {} file already exists".format("marilda3.pdf"))
    else:
        main("12/2020")
        change_path("marilda3.pdf")
    if os.path.isfile(
            r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\{}'.format("marilda4.pdf")):
        print("The {} file already exists".format("marilda4.pdf"))
    else:
        main("11/2020")
        change_path("marilda4.pdf")

salvar_faturas()
