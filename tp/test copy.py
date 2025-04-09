

import os
path = "usu_hogar_T324.txt"

"""for file in os.listdir(path_folder):"""



with open(path, "r") as fp:
    text = fp.read()

headers = [x.strip('"') for x in text.split("\n")[0].split(";")]

data = [{"Gender": "1", "Dasd": "sd"}]

for line in text.split("\n")[1:]:
    line_data = {}
    for c,value in enumerate(line.split(";")):
        value = value.strip('"')
        line_data[headers[c]] = value
    data.append(line_data)


def add_gender(data):
    for info in data:
        if not info.get("CH04"):
            continue
        gender = 'Masculino' if info["CH04"] == '1' else "Femenino"
        info["CH04_str"] = gender

add_gender(data)

import json
with open("data.json", "w") as fp:
    json.dump(data, fp)