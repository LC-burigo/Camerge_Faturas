import shutil

Paths = {"Marilda": r'C:\Users\burig\OneDrive\Documentos\Disciplina de comercialização'}


def change_path(data, agent):
    source = r'C:\Users\burig\Downloads\SegundaViaFatura.pdf'
    destination = find_path(data, agent)
    dest = shutil.move(source, destination)
    return dest


def find_path(data, agent):
    path_to_find = Paths[agent] + '\\' '{} - {}.pdf'.format(data.replace("/", "."), agent)
    return path_to_find