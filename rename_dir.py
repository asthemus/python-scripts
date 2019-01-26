import os

dire = input('Enter Directory name:')

if dire[-1] != '/':
	dire = dire + '/'

subs = input('any substring to check:')

for files in os.listdir(dire):
     if subs in files:
             src = dire + files
             dst = src
             dst = dst.replace(subs,'')
             os.rename(src,dst)
