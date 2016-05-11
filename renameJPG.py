# rename files with just plot code
#  from Command prompt type python, import os, the each line with colon after
#    This will fail each time a file with the same first 4 is encountered, 
#      and you will have to rename the secondary ones manually, move all the done ones
#      into a 'Done' folder you create, then run it again.

import os

while True:
    folderpath = raw_input('Folder path: ')
    print "\nChecking if folder path exists...\n"
    if os.path.exists(folderpath):
        print "Ok!\n"
        break;
    else:
        print "%s does not exist. Please enter a valid path.\n" % folderpath


print "Changing directory to %s\n" % folderpath

os.chdir(folderpath)

# have user enter file ending.  Usually either .JPG or .pdf
file_ending=raw_input('Enter file ending (with leading period, no quotes):  ')
print "\n%s\n" % file_ending

for filename in os.listdir("."):
    if filename.endswith(file_ending):
#        print "%s\n" % filename[:4]
        os.rename(filename,(filename[:4]+file_ending))
  