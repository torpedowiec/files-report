from pathlib import Path
import glob
import os
import pathlib
import json
from datetime import datetime

mounted_drives = [f'{d}:' for d in 'ABCDEFGHIJKLMNOPRSTUWXYZ' if os.path.exists(f'{d}:')]
todays_date = str(datetime.now())[:-7]

print('Currently there are following drives mounted in your OS: ' + str(mounted_drives))
drive_letter = input('Which drive would you like to analyze? Choose from list: ' + str(mounted_drives) + '\n')
print('Analysed drive set to: ' + drive_letter)

# Get files and directories inside given path into dictionary
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d['size'] = f'{round(os.path.getsize(path)/1000000,2)}MB'
        d['extension'] = f'{os.path.splitext(path)[1]}'
   # print(d)
    return d

def export_to_json():
    filename = "Files on " + drive_letter + " " + todays_date.replace(":","")
    with open(f'output/{filename}.json', "w+") as o:
        o.write(json.dumps(path_to_dict(f'{drive_letter}:/')))
        o.close()

# Return JSON with files and directories
dec1 = input("Do you want to export above result as a JSON file? (y/n)\n")
match dec1:
    case "y":
        export_to_json()
    case "n":
        print('OK, Imma quit then')
        quit()
    case _:
        print('Use y/n')
print("Nothing more to do, closing this app")
