## @Pacobits 10042018
## Rename all files in especific path

import os

path="e:\\MyWindows\\Downloads\\Telegram Desktop\\"
stringsearched="@pelisyseriescomolocos"
stringfinal=""
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if stringsearched in file:            
            print (os.path.join(r, file))
            print (os.path.join(r, file.replace(stringsearched,stringfinal)))
            os.rename(os.path.join(r, file),(os.path.join(r, file.replace(stringsearched,stringfinal))))

#for f in files:
#    print(f)