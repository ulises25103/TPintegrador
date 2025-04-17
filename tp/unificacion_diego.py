import os
from pathlib import Path

path_folder = Path('data_zip')

def get_data_structure(path_txt):
    with open(path_txt, "r", encoding="utf-8") as fp:
        text = fp.read()
    headers = [x.strip('"') for x in text.split("\n")[0].split(";")]

    data = []
    text_line = text.split("\n")[1:]
    for line in text_line:
        line_data = {}
        line_split = line.split(";")
        for key, value in enumerate(
            line_split
        ):  # me devuelve a lista con cada elemento con su indice.
            value = value.strip('"')  # me elimina las ""
            line_data[headers[key]] = (
                value  # me rellena el diccionario de manera que quede como key el header y el valor el value.
            )
        data.append(
            line_data
        )  # me rellena la lista de diccionarios, por cada linea en text, me genera un diccionario con su respectiva key y valor.
    return data


all_data = []
for file in os.listdir(path_folder):
    if file.endswith(".txt"):
        path_complete = f"{path_folder}/{file}"
        data = get_data_structure(path_complete)
        all_data.extend(data)

print(all_data)
