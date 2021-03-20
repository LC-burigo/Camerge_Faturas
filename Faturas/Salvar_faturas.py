from Faturas.Baixar_Faturas import main
from Faturas.Mudar_caminho import change_path
import os


def salvar_faturas(data):
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("1")):
        print("The marilda{}.pdf file already exists".format("1"))
    else:
        main(data)
        change_path("marilda1.pdf")
        print("marilda1.pdf was created")
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("2")):
        print("The marilda{}.pdf file already exists".format("2"))
    else:
        main(data)
        change_path("marilda2.pdf")
        print("marilda2.pdf was created")
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("3")):
        print("The marilda{}.pdf file already exists".format("3"))
    else:
        main(data)
        change_path("marilda3.pdf")
        print("marilda3.pdf was created")
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("4")):
        print("The marilda{}.pdf file already exists".format("4"))
    else:
        main(data)
        change_path("marilda4.pdf")
        print("marilda4.pdf was created")


salvar_faturas("01/2021")
