def exists_word(word, instance):
    result_list = list()
    for index in range(instance.__len__()):
        current = instance.search(index)
        ocorrencias = list()
        lines = current["linhas_do_arquivo"]

        for index, line in enumerate(lines):
            if (word.lower() in line.lower()):
                ocorrencias.append({"linha": index + 1})

        if (len(ocorrencias) > 0):
            result = {
                "palavra": word,
                "arquivo": current["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            }
            result_list.append(result)
    return result_list


def search_by_word(word, instance):
    result_list = exists_word(word, instance)
    if (len(result_list) <= 0):
        return result_list
    for index, result in enumerate(result_list):
        ocorrencias = result["ocorrencias"]
        for line in ocorrencias:
            lines = instance.search(index)["linhas_do_arquivo"]
            line["conteudo"] = lines[int(line["linha"]) - 1]
    result_list[index] = result
    return result_list
