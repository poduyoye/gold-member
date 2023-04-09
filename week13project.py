#!/usr/bin/env python3.7

#generate list of files from working directory

import os

cwd = os.getcwd()

files = []

for file_name in os.listdir(cwd):
    file_path = os.path.join(cwd, file_name)
    file_size = os.path.getsize(file_path)
    
    file_info = {'file_name': file_name, 
                 'file_path': file_path, 
                 'file_size': file_size,
}

    files.append(file_info)
    print(file_info, sep="\n")
