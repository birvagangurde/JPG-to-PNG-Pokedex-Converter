# FINAL-------------------------------------------
import sys
import os
from pathlib import Path
from PIL import Image 

#grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# check is new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')


# C:\Users\BIRVA\Desktop\Udemy\image-playground>python JPGtoPNGconverter.py Pokedex\\ new\\ path 
# has to be this so as to save all the new pictures in the new file made in the cmd












# import sys
# import os
# from pathlib import Path
# from PIL import Image 
 
# main_path = os.getcwd()
 
# image_path = f"{main_path}/Pokedex/"
# new_path = f"{main_path}/New/"
 
# Path(new_path).mkdir(parents=True, exist_ok=True)
 
 
# for filename in os.listdir(image_path):
#   clean_name = os.path.splitext(filename)[0]
#   img = Image.open(f'{image_path}{filename}')
#   img.save(f'{new_path}/{clean_name}.png', 'png')
#   print('all done!') 


























# 1st Part --------------------------------------
# import sys
# import os
# from PIL import Image

# #grab the first and second argument
# image_folder = sys.argv[1]
# output_folder = sys.argv[2]

# # print(image_folder, output_folder)

# # check is new/ exists, if not create
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # loop through Pokedex
# for filename in os.listdir(image_folder):
#     img = Image.open(f'{image_folder}{filename}')
#     img.save(f'{output_folder}{filename}', 'png')
#     print('all done!')



# loop through PokedexB


# convert images to png
# save to the new folder.