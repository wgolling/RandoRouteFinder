from map_controller import MapController
from map_objects import Region
from map_objects import Gate
from map_objects import Requisite
import unittest

class TestMapController(unittest.TestCase):

  def setUp(self):
    self.root  = Region("Root", 0)
    self.next1 = Region("Next 1", 1)
    self.next2 = Region("Next 2", 2)
    self.end   = Region("End", 3)
    self.root .add_gate(Gate(self.next1, {Requisite({"Req 1"})}))
    self.root .add_gate(Gate(self.next2, {Requisite({"Req 2"})}))
    self.next1.add_gate(Gate(self.end,   {Requisite({"Req 3"})}))
    self.next2.add_gate(Gate(self.end,   {Requisite({"Req 4"})}))
    self.mc = MapController(self.root, self.end)

  def test_fields(self):
    self.assertEqual(self.mc.root, self.root)
    self.assertEqual(self.mc.end , self.end)
    assert(self.mc.root.is_accessible)
    assert(not self.mc.end.is_accessible)

  def test_gain_item(self):
    self.mc.gain_item("Req 1")
    assert(self.next1.is_accessible)
    self.mc.gain_item("Req 3")
    assert(self.mc.end.is_accessible)
    assert(not self.next2.is_accessible)

  def test_lose_item(self):
    self.mc.gain_item("Req 1")
    self.mc.gain_item("Req 2")
    self.mc.gain_item("Req 3")
    self.mc.lose_item("Req 3")
    assert(not self.mc.end.is_accessible)
    assert(self.mc.root.is_accessible)
    assert(self.next1.is_accessible)
    assert(self.next2.is_accessible)

  def test_find_route(self):
    self.mc.gain_item("Req 1")
    self.mc.gain_item("Req 2")
    self.mc.gain_item("Req 3")
    route = self.mc.find_route(self.mc.end)
    self.assertEqual(route[0], self.root)
    self.assertEqual(route[1], self.next1)
    self.assertEqual(route[2], self.end)
    self.mc.lose_item("Req 3")
    route = self.mc.find_route(self.mc.end)
    assert(not bool(route))
    self.mc.gain_item("Req 4")
    route = self.mc.find_route(self.mc.end)
    self.assertEqual(route[0], self.root)
    self.assertEqual(route[1], self.next2)
    self.assertEqual(route[2], self.end)

  def test_count_items(self):
    self.assertEqual(self.mc.count_items(self.root), 0)
    self.mc.gain_item("Req 1")
    self.assertEqual(self.mc.count_items(self.root), 1)
    self.mc.gain_item("Req 2")
    self.assertEqual(self.mc.count_items(self.root), 3)
    self.mc.gain_item("Req 3")
    self.assertEqual(self.mc.count_items(self.root), 6)
    self.mc.gain_item("Req 4")
    self.assertEqual(self.mc.count_items(self.root), 6)
    self.mc.lose_item("Req 1")
    self.assertEqual(self.mc.count_items(self.root), 5)
    self.assertEqual(self.mc.count_items(self.next1), 4)




