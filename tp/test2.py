import os

path = "data/usu_individual_T324.txt"

with open (path, "r") as fp:
    text = fp.read()

headers = [x.strip('"') for x in text.split("\n")[0].split(";")]

data = []

text_line = text.split("\n")[1:]

for line in text_line:
    line_data = {}
    line_split = line.split(";")
    for key,value in enumerate(line_split): # me devuelve a lista con cada elemento con su indice.
        value = value.strip('"') # me elimina las ""
        line_data[headers[key]] = value # me rellena el diccionario de manera que quede como key el header y el valor el value.
    data.append(line_data) # me rellena la lista de diccionarios, por cada linea en text, me genera un diccionario con su respectiva key y valor.

hombres = 0
mujeres = 0

for persona in data:
    sexo = persona.get("CH04")  # puede ser '1', '2', o estar ausente
    if sexo == '1':
        hombres += 1
    elif sexo == '2':
        mujeres += 1

print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")