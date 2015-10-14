"""
File renaming script
Lindsay Ward, 12/09/2011
Modified 16/06/2014 - just use .replace instead of slicing the start; assume that's safe
"""

import os

# Remove start (from LearnJCU)
START_TEXT = "Project Milestone 2 (Full Site) & Peer Assessment_"
DIRECTORY = "/Users/sci-lmw1/Google Drive/CP2010/CP2010 2014/StudentWork/"

os.chdir(DIRECTORY)
for filename in os.listdir('.'):
    # get rid of LearnJCU's massive file name text and also the "attempt" text
    newName = filename.replace(START_TEXT, "").replace("attempt", "")
    # when testing, I use the print line and comment out the rename line, then I swap them over
    os.rename(filename, newName)
    # print(newName)

"""
# Replace %20 with space
os.chdir("/Users/sci-lmw1/Google Drive/JCU General/Resource Packages (Templates)/")
for filename in os.listdir('.'):
    newName = filename.replace("%20", " ")
    os.rename(filename, newName)
"""
