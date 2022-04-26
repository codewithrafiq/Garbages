from ast import Try
import os
from pathlib import Path
from konfik import Konfik
from project.utils.dataypes import *
from project import config, BASE_DIR


def generate_data():
    
    # define filepath
    filename = config.file.file_name
    filepath = BASE_DIR / config.file.file_name

    # clear the file content
    open(filepath, config.file.mode).close()
    
    # check the filesize
    fileSize = os.stat(filepath).st_size

    try:
        with open(filepath, config.file.mode) as file:
            while fileSize < config.file.size:                               #  filesize < 2MB
                function_list = [random_intnum, random_realnum, random_alphanumerics, random_alphabetical]
                data_type = random.choice(function_list)         # randomly choose a function to run
                output = data_type()
                file.write(output + ', ')
                fileSize = os.stat(filepath).st_size
                
            print('Final file size:', fileSize / 1000000, 'MB')
            file.close()
        
        print(filename)
        return {"filename": filename, "status": 200}

    except:
        return {"filename": None, "status": 500}

    

