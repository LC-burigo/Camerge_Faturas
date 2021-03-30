from Faturas.Baixar_Faturas import main
from Faturas.Mudar_caminho import change_path
import os


def salvar_faturas(data, agent):
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("1")):
        print("The marilda{}.pdf file already exists".format("1"))
    else:
        main(data)
        if os.path.isfile(r'C:\Users\burig\Downloads\SegundaViaFatura.pdf'):
            change_path("marilda1.pdf", "Marilda")
            print("marilda1.pdf was created")
        else:
            pass
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("2")):
        print("The marilda{}.pdf file already exists".format("2"))
    else:
        main(data)
        if os.path.isfile(r'C:\Users\burig\Downloads\SegundaViaFatura.pdf'):
            change_path("marilda2.pdf", "Marilda")
            print("marilda2.pdf was created")
        else:
            pass
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("3")):
        print("The marilda{}.pdf file already exists".format("3"))
    else:
        main(data)
        if os.path.isfile(r'C:\Users\burig\Downloads\SegundaViaFatura.pdf'):
            change_path("marilda3.pdf", "Marilda")
            print("marilda3.pdf was created")
        else:
            pass
    if os.path.isfile(r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\marilda{}.pdf'.format("4")):
        print("The marilda{}.pdf file already exists".format("4"))
    else:
        main(data)
        if os.path.isfile(r'C:\Users\burig\Downloads\SegundaViaFatura.pdf'):
            change_path("marilda4.pdf", "Marilda")
            print("marilda4.pdf was created")
        else:
            pass


salvar_faturas("03/2021")
