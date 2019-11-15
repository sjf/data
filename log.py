import sys

def _to_str(items):
  return " ".join(map(str, items))

def warn(*args):
  sys.stdout.write("WRN: %s\n" % (_to_str(args)))

def err(*args):
  sys.stdout.write("ERR: %s\n" % (_to_str(args)))

def log(*args):
  sys.stdout.write("LOG: %s\n" % (_to_str(args)))