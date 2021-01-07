import sys
import os
import errno
from PIL import Image

# Get inut and output directories from command line
inputDir = sys.argv[1]
outputDir = sys.argv[2]

if(not os.path.isdir(inputDir)):
    print(f'The first argument {inputDir} is not a directory')
    sys.exit(1)
    
if( not os.path.exists(outputDir)):
    os.makedirs(outputDir)

for filename in os.listdir(inputDir):
    print(f'The file {filename} is converted to png format.')
    img = Image.open(f'{inputDir}{filename}')
    filename_noextn=os.path.splitext(filename)[0]
    img.save(f'{outputDir}{filename_noextn}.png', 'png')