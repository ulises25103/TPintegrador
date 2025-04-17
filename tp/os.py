import os
import Path

current_path = os.getcwd
print(current_path)
exit()

for trimestre in os.listdir(current_path):
    archivos = os.listdir(os.path.join(current_path + trimestre))
    individual = [archivo for archivo in archivos if archivo.startwith("usu_individual")]

print(individual)