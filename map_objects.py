class Requisite:
  '''
  A class which keeps track of the items needed to tranverse a gate.
  Has methods corresponding to adding and removing items from the inventory,
  and a boolean which indicates if it is satisfied or not.
  '''
  def __init__(self, items):
    self.hard_items = items
    self.working_items = set(self.hard_items)
    self.is_satisfied = False

  def gain_item(self, item):
    if (item in self.working_items):
      self.working_items.remove(item)
    if not self.working_items:
      self.is_satisfied = True

  def lose_item(self, item):
    if item in self.hard_items:
      self.working_items.add(item)
      self.is_satisfied = False


class Gate:
  '''
  A class representing an edge on the world graph.
  It has a reference to a Region object on the "other side", a set of Requisite objects, 
  and an is_open boolean which is true if and only if any of the requisites are satisfied.
  '''
  def __init__(self, other_side, requisites):
    self.other_side = other_side
    self.requisites = requisites
    self.is_open = not bool(requisites)

  def gain_item(self, item):
    for req in self.requisites:
      req.gain_item(item)
      if req.is_satisfied:
        self.is_open = True

  def lose_item(self, item):
    still_open = False
    for req in self.requisites:
      req.lose_item(item)
      if req.is_satisfied:
        still_open = True
    self.is_open = still_open or not bool(self.requisites)


class Region:
  '''
  A class representing a node of the world graph.
  It primarily has a list of Gates and an is_accessible boolean which is maintained by a map controller.
  '''
  def __init__(self, name, chest_count):
    self.name = name
    self.chest_count = chest_count
    self.is_accessible = False
    self.gates = set()
    self.is_clear = False
    self.items_found = set()

  def add_gate(self, gate):
    self.gates.add(gate)

