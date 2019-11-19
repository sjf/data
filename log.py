import sys

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
   sys.stdout.write("%s: %s\n" % (level, _to_str(args)))