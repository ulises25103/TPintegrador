

import os
path_folder = "data"

for file in os.listdir(path_folder):
    path_complete = f'{path_folder}/{file}'
    print(path_complete)
