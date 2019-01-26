import os

for file in os.listdir('Folder_location'):
     if "sub_string" in file:
             src = 'Folder_location' + file
             dst = src
             dst = dst.replace('sub_string','')
             os.rename(src,dst)
