from queue import Queue

# do I need to import map_objects?

class MapController():

  def __init__(self, root, end):
    self.root = root
    self.root.is_accessible = True
    self.end  = end
    is_completable = False

  def recursive_gain_item(self, item, node, visited_nodes):
    visited_nodes.add(node)
    for gate in node.gates:
      gate.gain_item(item)
      o = gate.other_side
      if gate.is_open and node.is_accessible:
        o.is_accessible = True
        if o == self.end:
          is_completable = True
      if o not in visited_nodes:
        self.recursive_gain_item(item, gate.other_side, visited_nodes)

  def gain_item(self, item):
    self.recursive_gain_item(item, self.root, set())


  def recursive_lose_item(self, item, node, visited_nodes):
    visited_nodes.add(node)
    node.is_accessible = False
    for gate in node.gates:
      gate.lose_item(item)
      if gate.other_side not in visited_nodes:
        self.recursive_lose_item(item, gate.other_side, visited_nodes)

  def reset_accessibilities(self, node, visited_nodes):
    for gate in node.gates:
      if gate.is_open and node.is_accessible:
        gate.other_side.is_accessible = True
        if gate.other_side == self.end:
          is_completable = True
      if gate.other_side not in visited_nodes:
        self.reset_accessibilities(gate.other_side, visited_nodes)

  def lose_item(self, item):
    self.recursive_lose_item(item, self.root, set())
    self.is_completable = False
    self.root.is_accessible = True
    self.reset_accessibilities(self.root, set())


  def find_route(self, region):
    todo = Queue()
    visited_nodes = set()
    parents = dict()
    visited_nodes.add(self.root)
    todo.put(self.root)
    while not todo.empty():
      node = todo.get()
      for gate in node.gates:
        if not gate.is_open:
          break
        other = gate.other_side
        if other not in visited_nodes:
          visited_nodes.add(other)
          todo.put(other)
          parents[other] = node
    if not region in parents.keys():
      return None
    answer = list()
    current_node = region
    while current_node in parents.keys():
      answer.append(current_node)
      current_node = parents[current_node]
    answer.append(self.root)
    return list(reversed(answer))





