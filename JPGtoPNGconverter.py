"""
Script that converts JPG images to PNG images

- inputs: 	1. Path where JPG files are located
 			2. Path where PNG files will be saved

- output: 	Folder with PNG files	

"""

import sys 					# this is to parse folders as arguments
import os 					# this is to create the output folder
from PIL import Image		# to process images

#inputs
jpg_folder = os.path.abspath(sys.argv[1])
png_folder = os.path.abspath(sys.argv[2])

# create folder if does not exist
if not os.path.exists(png_folder):
	os.mkdir(png_folder)
	print(png_folder, 'succesfully created!')
else:
	print(png_folder, 'already exists!')	

# get list of files in jpg_folder
for file in sorted(os.listdir(jpg_folder)):
	print(file)
	pic = Image.open(os.path.join(jpg_folder,file))
	new_pic_name = file.split('.jpg')[0]
	pic.save( os.path.join(png_folder,new_pic_name+'.png'), format='PNG' )

print('Done!')

