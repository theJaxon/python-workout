# Write a function that takes a directory name (i.e., a string) as an argument. The
# function should return a dict in which the keys are the names of files in that
# directory, and the values are the file sizes. You can use os.listdir or glob
# .glob to get the files, but because only regular files have sizes, you’ll want to fil-
# ter the results using methods from os.path. To determine the file size, you can
# use os.stat or (if you prefer) just check the length of the string resulting from
# reading the file.

import pathlib, os

def dir_file_sizes(path):
    directory = pathlib.Path(path)
    return {
        item: os.stat(item).st_size
        for item in directory.iterdir()
        if os.path.isfile(item)
    }

print(dir_file_sizes('/tmp'))