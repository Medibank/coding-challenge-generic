#!/usr/bin/env python
# coding: utf-8

# ## Requirements
# I am going to:
# - Write a script to search through a directory (and subdirectories) of files.
# - Output the list of unique strings with descending order of occurrences next to them
# - Only strings with more than 2 occurrences should be reported
# - Words should be case insensitive for counting purposes
# 
# 
# Note: I will use python in this project.

# ## Project description:
# 
# Below program, should go through all the folders/subdirectories and fetch all the existing file names. So I create a recursive function to call itself over and over to reach the last root of each directory. During this process, I assumed those items with "." are files, like: .text, .pdf,... and others are folders. But to consider those files without ".", I use try / except block. It means that if it has no "." but still is a file name, it face **NoSuchDirectory alarm**, so goes to except and add it as file name and continue.
# 
# So it start with the main given path, via using the **os libraries** it gets list of the directories and save it in a list. Then I apply a **recursive function** on each of the item. This function first checks if it is a file or a folder. If it is a file it adds its name to a list of file names, else it will **change directory to this sub directory through os library** and recursively do the same for each element. 
# 
# This will continue till the time that the last item in one sub directory is checked as file. So the name will add to name list and now it needs to go one step back to check other items in the higher directory, that I call it the main root for this sub directory.
# 
# Please note, each time it change directory to a folder, it gets the total number of items inside it and after applying the function on each item it decrease the number to make sure all items are checked.
# 
 
# After it backs to the main provided path, and applied function on all the items, we will have a list of all the file names. So I will create a dictionary with file names as the keys and number of occurrence as the value. Then make this dictionary as a list of tuples (file_name, occurrence_num). After sorting this list based on number of occurrences in descending order, it will print only those with **> 2** repetition.





# Importing os libraries
import os

# Defining a function to check each items recursively and update file name list
def check(name):
    """
    This function check each item, update file name and call itself recursively for folders
    """
    global path, root_path      # I need to use these variables as global to be used inside and outside of the function
    global file_names

    # It must be case insensitive, so first I make the name lower case.
    name = name.lower()

    # To evaluate this item is file or folder, it checks whether "." is in the file name?
    if len(name.split(".")) !=1:             # If it is a file
        file_names.append(name)              # add file name to the list
    else:                                    # If it is a folder
        
        try:
            
        # If this name has no "." but still is a file name, it faced "NoDirectory" error, that I consider it in this try/except 

            root_path = path                     # It keeps this path as the root path for the next sub directory
            path = path+"/"+name                 # create path to change directory to this folder          
            os.chdir(path)                      # change directory to this folder
            folder_inside = os.listdir()        # list items inside the directory
            num = len(folder_inside)            # number of items in this subdirectory
            if num != 0:                        # if the folder is not empty, it go through each of the items
                for i in folder_inside:         # It iterates through all items inside it
                    check(i)
                    num -= 1                    # after checking each item, decrease the number
                    if num ==0:                 # If all items are checked
                        # When all items inside the folder are read, It needs to change the path to the root, one step back
                        current_path = path.split("/")  # the last folder name after / must be removed after spliting on /
                        current_path.pop()
                        root_path = "/".join(current_path)   # for the root address by joing with /
                        path = root_path                # go to root to check other items
            else:                # if it is an empty folder
                path = root_path   # It go to the root path to check other items
                
        except Exception:
            file_names.append(name)
            pass


# Now I need to enter the directory address in this format  D:/A/B/......

path ="C:/Program Files"
#  first it change directory to this address and apply the function on it.
os.chdir(path)
dir_file = os.listdir()
file_names = []
for item in dir_file:
    check(item)


# ### Create occurrence dictionary:
# Now I have list of all file names, so at the next step I create a dictionary and add each item occurrence for each individual file name.


file_names_dict = {}         # It creates an empty dictionary
for file_name in file_names:   # for each item in the file name list
    if file_name in file_names_dict: 
        # if file is a rpeated file name, adds its value to one more
        file_names_dict[file_name]+=1
    else:
        # If it is not included in the dictionary, add it with value 1 as new occurance file name
        file_names_dict[file_name] = 1      

# It sort the list of tuples format of the file name dictionary [(,),(,),..] based on the value, 2nd item at each tuple
new_file_names = sorted(file_names_dict.items(), key = lambda item : item[1], reverse=True)

# It filtered for those file names with more than 2 occurrence
filtered_file_names = [item for item in new_file_names if item[1] > 2]

# Now it print from the most occurrence file name at below format:
for item in filtered_file_names:
    print(item[0],"  ", item[1])