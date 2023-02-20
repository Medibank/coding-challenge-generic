# Medibank Coding Challenge
### Name: Niousha Dastan

## Note: I will use python in this project.


## Overview
Sort through a list of files in a folder structure
- Write a script to search through a directory (and subdirectories) of files.
- Output the list of unique strings with descending order of occurrences next to them
- Only strings with more than 2 occurrences should be reported


## Requirements
 I am going to:
 - Write a script to search through a directory (and subdirectories) of files.
 - Output the list of unique strings with descending order of occurrences next to them
 - Only strings with more than 2 occurrences should be reported
 - Words should be case insensitive for counting purposes
 

## Project description:

-Below program, should go through all the folders/subdirectories and fetch all the existing file names. So I create a recursive function to call itself over and over to reach the last root of each directory. During this process, I assumed those items with "." are files, like: .text, .pdf,... and others are folders. But to consider those files without ".", I use try / except block. It means that if it has no "." but still is a file name, it face **NoSuchDirectory alarm**, so goes to except and add it as file name and continue.
 
So it start with the main given path, via using the **os libraries** it gets list of the directories and save it in a list. Then I apply a **recursive function** on each of the item. This function first checks if it is a file or a folder. If it is a file it adds its name to a list of file names, else it will **change directory to this sub directory through os library** and recursively do the same for each element. 

This will continue till the time that the last item in one sub directory is checked as file. So the name will add to name list and now it needs to go one step back to check other items in the higher directory, that I call it the main root for this sub directory.
 
Please note, each time it change directory to a folder, it gets the total number of items inside it and after applying the function on each item it decrease the number to make sure all items are checked.

After it backs to the main provided path, and applied function on all the items, we will have a list of all the file names. So I will create a dictionary with file names as the keys and number of occurrence as the value. Then make this dictionary as a list of tuples (file_name, occurrence_num). After sorting this list based on number of occurrences in descending order, it will print only those with **> 2** repetition.