# Use a dict comprehension to create a dict in which the keys are usernames and
# the values are (integer) user IDs, based on a Unix-style /etc/passwd file. Hint:
# in a typical /etc/passwd file, the usernames are the first field in a row (i.e.,
# index 0), and the user IDs are the third field in a row (i.e., index 2). If you need
# to download a sample /etc/passwd file, you can get it from http://mng.bz/
# 2XXg. Note that this sample file contains comment lines, meaning that you’ll
# need to remove them when creating your dict.

def names_ids(path):
 return {   line.split(':')[0]: line.split(':')[2]
            for line in open(path)
        }

print(names_ids('/etc/passwd'))