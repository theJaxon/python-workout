import os , glob, arrow

# Shows how many days since a file has been last modified

# Empty dictionary to store file names as keys and last modified time in days
files_info = {}

def dir_info(dir_name):
  for file in glob.glob(f'{dir_name}/*'):
    if os.path.isfile(file):
      files_info[file] = (arrow.now() - arrow.get(os.stat(file).st_mtime)).days

  return files_info

print(dir_info('/tmp'))