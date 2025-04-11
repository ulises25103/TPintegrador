from pathlib  import Path
import csv
file = Path('tp')/'data'/'usu_individual_T216.txt'
CH04_str= ''
list_disc_indi = []
with open (file, encoding="utf-8") as data:
    reader = csv.DictReader(data, delimiter=';')
    for row in reader:
        list_disc_indi.append(row)

for i,dict in enumerate(list_disc_indi):
    if list_disc_indi[i]['CH04'] == '1': # valor 1 = Masculino, valor 2 = Femenino.
            list_disc_indi[i]['CH04_str'] = 'Masculino'
    else:
        list_disc_indi[i]['CH04_str'] = 'Femenino'
    print(list_disc_indi[i]['CH04_str'])


    
        