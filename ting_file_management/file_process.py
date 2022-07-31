import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.__len__()):
        if (instance.search(index)["nome_do_arquivo"] == path_file):
            return
    text = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }
    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    if (instance.__len__() <= 0):
        print("Não há elementos", file=sys.stdout)
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if((instance.__len__() - 1) < position):
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.search(position), file=sys.stdout)
