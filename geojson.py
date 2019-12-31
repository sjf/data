import pygeoj

def read_geojson(filename, fun=None):
  geojson = pygeoj.load(filepath=filename)
  if fun is not None:
    for feature in geojson:
      fun(feature)
  return geojson

def write_geojson(geojson, filename):
  geojson.save(filename)

def strip_properties(geojson, keep):
  for feature in geojson:
    new_properties = {}
    for k in keep:
      if k in feature.properties:
        new_properties[k] = feature.properties[k]
    feature.properties = new_properties

def convert_properties(geojson, convert_dct):
  for feature in geojson:
    for name,converter in convert_dct.items():
      if type(converter) == type(tuple()):
        new_prop,converter = converter
      else:
        new_prop = name
      if name in feature.properties:
        feature.properties[new_prop] = converter(feature.properties[name])


