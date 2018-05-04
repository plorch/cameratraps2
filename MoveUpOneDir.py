import csv, os, shutil
"""
This copies files out of a directory they are in to the directory above and 
 then deletes the empty plot directory.
"""
while True:
    folderpath = raw_input('Folder path: ')
    print "Checking if folder path exists..."
    if os.path.exists(folderpath):
        print "Ok!"
        break;
    else:
        print "%s does not exist. Please enter a valid path.\n" % folderpath
        break;


print "Changing directory to %s" % folderpath

os.chdir(folderpath)

# have user enter file ending.  Usually either .JPG or .pdf
file_ending=raw_input('Enter file ending (with leading period, no quotes):  ')
print "File ending: %s\n" % file_ending

for root, dirs, files in os.walk(folderpath):
    dirlist=dirs
    for filename in files:
        if filename.endswith(file_ending) and not filename.startswith('.'):
            filepath = os.path.join(root,filename)
            dest_dir = os.path.dirname(os.path.dirname(filepath))
            shutil.move(filepath, dest_dir)
            print "Filepath %s" % filepath
            print " copied to %s" % dest_dir
        else:
            print "File %s not copied." % os.path.join(root,filename)
            if len(os.listdir(root)) == 0 or (len(os.listdir(root)) == 1 and os.listdir(root)[0] == 'Thumbs.db'):
                os.remove(os.path.join(root,'Thumbs.db'))
                os.rmdir(root)
                print "Dir %s deleted.\n" % root
#            break