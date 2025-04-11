from pathlib  import Path
import csv
file = Path('tp')/'data'/'usu_individual_T324.txt'
CH04_str= ''
list_disc = []
with open (file, encoding="utf-8") as data:
    reader = csv.DictReader(data, delimiter=';')
    for row in reader:
        list_disc.append(row)

for i,dict in enumerate(list_disc):
    if list_disc[i]['CH04'] == '1': # valor 1 = Masculino, valor 2 = Femenino.
            list_disc[i]['CH04_str'] = 'Masculino'
    else:
        list_disc[i]['CH04_str'] = 'Femenino'
    print(list_disc[i]['CH04_str'])


    
        