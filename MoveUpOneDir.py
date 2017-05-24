import csv, os
"""
This does not work at all !!!
This copies files out of a directory they are in to the directory above
"""
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

for root, dirs, files in os.walk(folderpath):
    for filename in files:
        if filename.endswith(file_ending) and not filename.startswith('.'):
            filepath = os.path.join(root, filename)
            dest_dir = os.path('..')
            os.rename(filepath, os.path.join(dest_dir, filename))
        else:
            print "Nothing worked!"
    break