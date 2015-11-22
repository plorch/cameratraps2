# rename files with just plot code
#  from Command prompt type python, import os, the each line with colon after
#    This will fail each time a file with the same first 4 is encountered, 
#      and you will have to rename the secondary ones manually, move all the done ones
#      into a 'Done' folder you create, then run it again.
import os
for filename in os.listdir("."):
 if filename.endswith(".JPG"):
  os.rename(filename,(filename[:4]+".JPG"))
  