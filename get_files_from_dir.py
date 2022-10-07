from pathlib import Path
import glob
import os
import pathlib
import json
from datetime import datetime

path_to_drive = str(pathlib.PureWindowsPath(r'E:/'))
todays_date = str(datetime.now())
print('Your drive letter is set to: ' + path_to_drive)
print('Right now it\'s: ' + str(todays_date))
# Get files and directories inside given path in JSON format
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d['size'] = f"{round(os.path.getsize(path)/1000000,2)}MB"
        d['extension'] = f"{os.path.splitext(path)[1]}"
    return d

def export_to_json():
    filename = "Files on " + path_to_drive.replace(":\\","") + " " + todays_date[:-7].replace(":","")
    with open(f"output/{filename}.json", "w+") as o:
        o.write(json.dumps(path_to_dict(path_to_drive)))
        o.close()

# Return JSON with files and directories
#print(json.dumps(path_to_dict(path_to_drive)))
dec1 = input("Do you want to export above result as a JSON file? (y/n)")
match dec1:
    case "y":
        export_to_json()
    case "n":
        print("OK, Imma quit then")
        quit()
    case _:
        print('Use y/n')
print("Let's do sth else")



"""
try:
    p = Path(path_to_drive)
    print('Directories in drive plugged to this PC', end=" ")  
    list_dirs = [x for x in p.iterdir() if x.is_dir()]
    print(list_dirs)
    text_files_in_dir = [x for x in p.rglob('*.txt') if x.is_file()]
    print('There are', len(text_files_in_dir), 'text files in ', p)
    print('Path of main object',p)
    print("Pathlib object type of:" , type(p) , "has been set.")
except:
    print("Tried to set Path() Pathlib object. Didn't work.")
"""

# Messing with glob() in case pathlib() won't be sufficient
#list_ = glob.glob(path_to_drive + "*")
#print(os.path)