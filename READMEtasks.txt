READMEtasks.txt

* Copy into appropriate named folders on folder (e.g., C:\Users\pdl\Documents\GitHub\cameratraps2\2012PCAP_Plot_Pictures and C:\Users\pdl\Documents\GitHub\cameratraps2\2012DataSheetsFinal) that will update to when you sync github plorch.github.io/cameratraps2/
* Run renameJPG.py on directory with .pdf files
  * you will need to move done ones into temporary done folder, then run again, every time a file with the same 4 (plot number) is encountered.
* Add line to index.html for new year
* In C:\Users\pdl\Documents\GitHub\cameratraps2\2012PCAP_Plot_Pictures, go into each reservation folder and delete voucher or encroachment folders and manually rename to 4 number reservation names (delete date info)
* Duplicate latest year's secondary page (e.g., group2011.html)
  * Global replace all 2011 with 2012
  * Fix links to match what is now in image and pdf folders
    * In Sublime Text highlight site number and `Ctl D` enough times to highlight all you want to change then type new number
  * If there are multiple images remove date information from name but add image number (to match with what is in field notes) and add secondary links for additional images
  * Use 'No Image' if none exists
  * Move all .jpg files out of numbered folder into reservation folder
    * I have been doing this by hand, since I could not get the os.walk script I tested to work
    * Open a file explorer of the reservation subdirectory
    * Open command window to same place
      * use `move 1203\1203.JPG .` to move up (using tab to autocomplete)
    * delete directories after checking that you have not left anything inside them
  * Check to see that all .pdf files in folder are linked to
  * Add secondary links for cases where there are two .pdf files (where Sarah redid a plot?)
  * Check to see that folder names used in 2012PCAP_Plot_Pictures match folder names (remove spaces from folder names, etc.)