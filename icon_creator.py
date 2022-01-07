from PIL import Image
import os
import shutil
import sys

filename = sys.argv[1]

real_filename = filename.split('/')[-1]

given_sizes = [(40,40),(60,60),(58,58),(87,87),(80,80),(120,120),(180,180),(1024,1024)]

dir = (filename.split('.')[0]) + " Icons/"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.mkdir(dir)

image = Image.open(real_filename)
for i in range(len(given_sizes)):
    resized_image = image.resize(given_sizes[i])
    resized_image.save(dir+'/'+'tips-icon_'+str(given_sizes[i][0])+'x'+str(given_sizes[i][0])+'.png')