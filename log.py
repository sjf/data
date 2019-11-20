import sys
from datetime import datetime

def warn(*args):
  _log("LOG", args)

def err(*args):
  _log("ERR", args)

def log(*args):
  _log("LOG", args)

def fail(*args):
  err(args)
  sys.exit(1)

def _to_str(items):
  return " ".join(map(str, items))

def _log(level, args):
  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  sys.stdout.write("%s %s: %s\n" % (level, date, _to_str(args)))