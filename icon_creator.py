from PIL import Image
import os
import shutil
import sys

# Grabs file name from command line
filename = sys.argv[1]

# removes file path before file name and extension
real_filename = filename.split('/')[-1]

# initialise array for current required image sizes (in future will be in a settings.txt file)
given_sizes = [(40,40),(60,60),(58,58),(87,87),(80,80),(120,120),(180,180),(1024,1024)]

# creates new folder regardless of whether or not a folder with the same name exists (will be changed to make (1) appear at end)
dir = (filename.split('.')[0]) + " Icons/"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.mkdir(dir)

# stores inputted image data in image variable
image = Image.open(real_filename)

# creates a new file for each given size in given sizes
for i in range(len(given_sizes)):
    resized_image = image.resize(given_sizes[i])
    resized_image.save(dir+'/'+'tips-icon_'+str(given_sizes[i][0])+'x'+str(given_sizes[i][0])+'.png')
