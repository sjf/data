import sys
import os
from data.log import *

def get_arg(i, default):
  if i < len(sys.argv):
    return sys.argv[i]
  return default

def run(cmd):
  log('Running', cmd)
  res = os.system(cmd)
  if res != 0:
    sys.exit(res)