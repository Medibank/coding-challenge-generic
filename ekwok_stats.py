"""
Name        : ekwok_stats.py
To Run      : python3 ekwok_stats.py [dirname]
Author      : Eddy Kwok
"""

import os
import sys
import glob
import json
import logging

MIN_COUNT = 3       # minimum count qualify for print
DEFAULT_DIR = "."   # default folder

logging.basicConfig(level=logging.DEBUG)  # Logging Level: INFO, DEBUG, ...


def getFilenames(dirname):
    # Create Filenames Dict with filename as key, to do counting easily
    # format: {filename1: 1, filename2: 2, ... }
    dic_filenames = {}
    try:
        for filePath in glob.iglob(dirname + '**/**', recursive=True):
            # filter filenames only
            if os.path.isfile(filePath):
                # pick only filename and convert it to lower case
                filename = filePath.split("/")[-1].lower()
                try:
                    dic_filenames[filename] += 1
                except:  # key not existed
                    dic_filenames[filename] = 1
    except Exception as e:
        logging.error(e)

    logging.debug("getFilenames >> dic_filenames: {}".format(dic_filenames))
    return dic_filenames


def getCounters(dic_filenames):
    # Create Counter Dict with counter as key, with value: concatenated filenames, sort key asc
    # format: { 1:"filename1,filename2",... }
    dic_counters = {}
    try:
        for filename, count in dic_filenames.items():
            if count >= MIN_COUNT:
                try:
                    dic_counters[count] = dic_counters[count] + "," + filename
                except:  # key not existed
                    dic_counters[count] = filename

        # convert to json to sort then convert back to dict
        dic_counters = json.loads(json.dumps(dic_counters, sort_keys=True))
    except Exception as e:
        logging.error(e)
    logging.debug("getCounters >> dic_counters: {}".format(dic_counters))
    return dic_counters


def main():
    try:
        # if no directory argument entered, use current folder
        root_dir = DEFAULT_DIR
        if len(sys.argv) > 1:
            root_dir = sys.argv[1]

        dic_filenames = getFilenames(root_dir)
        dic_counters = getCounters(dic_filenames)

        # enumerate dic in descending order
        for count, filenames in reversed(dic_counters.items()):
            for filename in filenames.split(","):
                print(filename, count)

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    main()
