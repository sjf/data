import sys
import os
from data.log import *

# Functional programming

def mapl(f,l):
  """ Map `f` to list `l` and return a list."""
  return list(map(f,l))

# File I/O
def read_lines(f):
  """ Returns a list of lines from `f` with newlines stripped."""
  with open(f) as fh:
    lines = fh.readlines()
    return rstripl(lines)

# Stringly typed data

def rstripl(l):
  return mapl(lambda x:x.rstrip(), l)

def splitpairs(l,delim="="):
  return [ tuple(x.split(delim,1)) for x in l ]

def splitpairsws(l):
  return [ tuple(x.split(None,1)) for x in l ]

def filter_dict(d, key_filter):
  res = {}
  for k,v in d.items():
    if k not in key_filter:
      res[k] = v
  return res

def printlines(x):
  if type(x) == type({}):
    _printdict(x)
  elif type(x) == type([]) or type(x) == type(()):
    _printlist(x)
  else:
    print(x)

def _printdict(d):
  keys = sorted(d.keys())
  for k in keys:
    print(f"{k} = {d[k]}")
  print()

def _printlist(l):
  for x in l:
    print(x)
  print()

# OS related

def isfile(f):
  return os.path.isfile(f)

def get_arg(i, default):
  if i < len(sys.argv):
    return sys.argv[i]
  return default

def run(cmd):
  log('Running', cmd)
  res = os.system(cmd)
  if res != 0:
    sys.exit(res)

def getpath():
  return os.getenv('PATH').split(os.pathsep)

