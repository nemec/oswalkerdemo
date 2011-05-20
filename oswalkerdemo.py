import os

"""
This is a demo of the os.walk function in Python.
Since it's a little confusing to figure out what the root, dirs, and files mean
during each iteration of the function, I put together a simple filesystem
display that prints the provided folder then all files and folders beneath it.

Each subsequent layer is indented two spaces more than the layer above it.
"""

path = "./test/"

if path[-1] == os.sep:
  path = path[:-1] # remove ending slash if present


base_depth = path.count(os.sep)
# base depth is the number of / (or \) in the provided path
# we need to count them so that indentation starts out as "none" for root

def find_basename(path):
  # Chop off everything before the last / (or \)
  return path[path.rfind(os.sep)+1:]

for current_directory, dirs_in_curr_dir, files_in_curr_dir in os.walk(path):
  depth = current_directory.count(os.sep) - base_depth

  # ("  " * depth) : concatenates "depth" copies of "  " together
  print "  " * depth + find_basename(current_directory) + os.sep

  for f in files_in_curr_dir:
    print "  " * (depth+1) + find_basename(f)

