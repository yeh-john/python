# Import modules
import os
import sys

# Set directory
folder = "."

# Start main program
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    # Setting file type  (EX: .cache to .jpg)
    newname = infilename.replace('.cache', '.jpg')
    output = os.rename(infilename, newname)
