import csv

def to_int(s, row=None):
  try:
    return int(s)
  except ValueError:
    print("Not int: '" + s + "'", row if row is not None else "")
    return None

def to_float(s, row=None):
  try:
    return float(s)
  except ValueError:
    print("Not float: '" + s + "'", row if row is not None else "")
    return None

def read_csv(file, fun):
  with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
      fun(row)

def write_csv(file, dicts, sort_field=None):
  assert len(dicts) >= 1
  out = []
  i = 0
  for dct in dicts:
    key = dct[sort_field] if sort_field is not None else i
    out.append((key, dct))
    i += 1
  out = sorted(out)
  headers = sorted(dicts[0].keys())

  with open(file, mode='w') as file:
      writer = csv.DictWriter(file, fieldnames=headers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      writer.writeheader()
      for key,dct in out:
        writer.writerow(dct)

