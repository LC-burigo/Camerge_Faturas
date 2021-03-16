import shutil


def change_path(nome_arquivo):
    source = r'C:\Users\burig\Downloads\SegundaViaFatura.pdf'
    destination = r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização\{}'.format(nome_arquivo)
    dest = shutil.move(source, destination)
    return dest



