class UnionFind:
  class Entry:
    def __init__(self, id):
      self.id = id
      self.parent = id
      self.size = 1
    def __repr__(self):
      return "{" + repr(self.id) + "}"

  def __init__(self, ids=[]):
    self.entries = {}
    map(self._add, ids)

  def union(self,a_id,b_id):
    pa = self._find(self._get(a_id))
    pb = self._find(self._get(b_id))
    if pa == pb:
      return
    big,small = pa,pb
    if pb.size > pa.size:
      big,small = pb,pa
    big.parent = small.id
    small.size += big.size

  def sets(self):
    sets = {}
    for entry in self.entries.values():
      parent = self._find(entry)
      if parent.id not in sets:
        sets[parent.id] = []
      sets[parent.id].append(entry.id)
    return list(sets.values())

  def _find(self,a):
    if a.parent == a.id:
      return a
    parent = self._find(self._get(a.parent))
    a.parent = parent.id
    return parent

  def _get(self, id_):
    if id_ not in self.entries:
      self._add(id_)
    return self.entries[id_]

  def _add(self,id_):
    self.entries[id_] = self.Entry(id_)