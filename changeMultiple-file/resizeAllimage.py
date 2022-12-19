# Import modules
from PIL import Image
import os
import sys

# Set directory
path = "."
dirs = os.listdir(path)

# Start main program
for item in dirs
  if os.path.isfile(path+item):
    img = Image.open(path+item)
    f, e = os.path.splitext(path+item)
    imResize = im.resize((500,500),Image.ANTIALIAS)
    imResize.save(f + 'resized.png', 'PNG', quality=100)
