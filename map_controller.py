from queue import Queue

class MapController():
  '''
  A controller class to implement graph functions on the game map.
  '''
  def __init__(self, root, end):
    self.root = root
    self.root.is_accessible = True
    self.end  = end
    is_completable = False


  # Item acquisition

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
    '''
    Has the effect of adding an item to the inventory.
    Updates all the Gates and Regions in the graph.
    '''
    self.recursive_gain_item(item, self.root, set())


  # Item loss

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
    '''
    Has the effect of removing an item from the inventory.
    Updates all the Gates and Regions in the graph.
    '''
    self.recursive_lose_item(item, self.root, set())
    self.is_completable = False
    self.root.is_accessible = True
    self.reset_accessibilities(self.root, set())


  # Route finding

  def find_route(self, region):
    '''
    Returns a list representing a shortest path to the given region if it is accessible, 
    and None otherwise.
    '''
    if not region.is_accessible:
      return None
    todo = Queue()
    visited_nodes = set()
    parents = dict()
    visited_nodes.add(self.root)
    todo.put(self.root)
    while not todo.empty():
      node = todo.get()
      for gate in node.gates:
        if not gate.is_open:
          continue
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


  # Item counting

  def recursive_count_items(self, node, visited_nodes):
    visited_nodes.add(node)
    recursive_tally = 0
    for gate in node.gates:
      if not gate.is_open:
        continue
      other = gate.other_side
      if other in visited_nodes:
        continue
      recursive_tally += self.recursive_count_items(other, visited_nodes)
    return recursive_tally + node.chest_count

  def count_items(self, region):
    '''
    Returns the number of items accessible from the given region.
    '''
    return self.recursive_count_items(region, set())




