from PIL import Image
import os
import shutil
import sys
from ast import literal_eval

# Grabs file name from command line
filename = sys.argv[1]

# removes file path before file name and extension
real_filename = filename.split('/')[-1]

# initialise array for current required image sizes
f = open("settings.txt","r")
sizes = f.read().split('\n')
f.close()

for i in range(len(sizes)):
    sizes[i] = (sizes[i]).split(',')

# creates new folder to store icons (named after the initial file.)
dir = (filename.split('.')[0]) + " Icons/"
x = True
i = 1
new_dir = dir
while x == True:
    if os.path.exists(new_dir):
        new_dir = str(dir[:-1]+" ("+str(i)+")")
        i += 1
    else:
        os.mkdir(new_dir)
        x = False

# stores inputted image data in image variable
image = Image.open(real_filename)

# creates a new file for each given size in given sizes
for i in range(len(sizes)):
    resized_image = image.resize((int(sizes[i][0]),int(sizes[i][1])))
    resized_image.save(dir+'/'+'tips-icon_'+sizes[i][0]+'x'+sizes[i][0]+'.png')
