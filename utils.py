import sys

def get_arg(i, default):
  if len(sys.argv) < i:
    return sys.argv[i]
  return default