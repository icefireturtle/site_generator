import os
import shutil
import time


def copy_static(source, destination):

    contents = os.listdir(source)
        
    print(f"static contents:\n {contents}")
    time.sleep(1)
    print(f"copying contents {contents}")
    time.sleep(1)

    for copy in contents:
        copy_path = os.path.join(source, copy)
        is_file = os.path.isfile(copy_path)
        if is_file == True:
            print(f"copying {copy}...")
            shutil.copy(copy_path, destination)
            time.sleep(1)
        else: 
            copy_destination = os.path.join(destination, copy)
            print(f"creating desintation {copy_destination}...")
            os.mkdir(copy_destination)
            copy_static(copy_path, copy_destination)



