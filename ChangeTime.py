import pandas as pd
import datetime
import os
import pathlib

# Put the files that are to have their access time and modification time changed in a folder named "input"

def main():
    input_path_name = 'input'
    
    for file in os.listdir(input_path_name):
        filename = os.fsdecode(file)
        file_path = os.path.join(pathlib.Path().absolute(),input_path_name, filename)
    
        print(file_path)
        
        access_time = datetime.datetime.now().timestamp()
        modification_time = datetime.datetime.now().timestamp()
        os.utime(file_path, (access_time, modification_time))
        
        
if __name__ == "__main__":
    main()
