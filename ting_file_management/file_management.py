import sys
import os

def txt_importer(path_file):
    if(path_file[-3:] != "txt"):
        print("Formato inválido", file=sys.stderr)
    else:
        if not os.path.exists(path_file):
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        else:
            with open(path_file, 'r', encoding="utf-8") as file:
                lines = file.readlines()
                return [line.replace("\n", "") for line in lines]
