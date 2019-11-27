import sys

def get_arg(i, default):
  if i < len(sys.argv):
    return sys.argv[i]
  return default