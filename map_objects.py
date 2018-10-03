class Requisite:

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

  def __init__(self, name, chest_count):
    self.name = name
    self.chest_count = chest_count
    self.is_accessible = False
    self.gates = set()
    self.is_clear = False
    self.items_found = set()

  def add_gate(self, gate):
    self.gates.add(gate)

