from map_objects import Requisite
from map_objects import Gate 
from map_objects import Region
import unittest

class TestRequisite(unittest.TestCase):

  def setUp(self):
    self.test_req = Requisite({"Test Item 1", "Test Item 2"})

  def test_fields(self):
    item_set = self.test_req.working_items
    assert("Test Item 1" in item_set)
    assert("Test Item 2" in item_set)
    assert("Test Item 3" not in item_set)

    hard_item_set = self.test_req.hard_items
    assert("Test Item 1" in item_set)
    assert("Test Item 2" in item_set)
    assert("Test Item 3" not in item_set)

    assert(not self.test_req.is_satisfied)

  def test_gain_item(self):
    self.test_req.gain_item("Test Item 1")
    assert(not self.test_req.is_satisfied)
    self.test_req.gain_item("Test Item 3")
    assert(not self.test_req.is_satisfied)
    self.test_req.gain_item("Test Item 2")
    assert(self.test_req.is_satisfied)

  def test_lose_item(self):
    self.test_req.gain_item("Test Item 1")
    self.test_req.gain_item("Test Item 2")
    assert(self.test_req.is_satisfied)
    self.test_req.lose_item("Test Item 3")
    assert(self.test_req.is_satisfied)
    self.test_req.lose_item("Test Item 2")
    assert("Test Item 2" in self.test_req.hard_items)
    assert("Test Item 2" in self.test_req.working_items)
    assert(not self.test_req.is_satisfied)


class TestGate(unittest.TestCase):

  def setUp(self):
    dummy_region   = Region("Dummy Region", 0)
    dummy_req1     = Requisite({"Test 1", "Test 2"})
    dummy_req2     = Requisite({"Test 1", "Test 3"})
    self.test_gate = Gate(dummy_region, {dummy_req1, dummy_req2})
    self.free_gate = Gate(dummy_region, set())

  def test_fields(self):
    assert(not self.test_gate.is_open)
    self.assertEqual(self.test_gate.other_side.name, "Dummy Region")
    assert(self.free_gate.is_open)

  def test_gain_item(self):
    self.test_gate.gain_item("Test 1")
    assert(not self.test_gate.is_open)
    self.test_gate.gain_item("Test 2")
    assert(self.test_gate.is_open)
    self.test_gate.gain_item("Test 3")
    assert(self.test_gate.is_open)
    self.test_gate.gain_item("Test 4")
    assert(self.test_gate.is_open)

  def test_lose_item(self):
    self.test_gate.gain_item("Test 1")
    self.test_gate.gain_item("Test 2")
    self.test_gate.gain_item("Test 3")
    self.test_gate.lose_item("Test 2")
    assert(self.test_gate.is_open)
    self.test_gate.lose_item("Test 1")
    assert(not self.test_gate.is_open)

    self.free_gate.lose_item("Test 1")
    assert(self.free_gate.is_open)


class TestRegion(unittest.TestCase):

  def setUp(self):
    self.test_region = Region("Test Region", 0)
    self.other_region = Region("Other Region", 0)

  def test_fields(self):
    self.assertEqual(self.test_region.name, "Test Region")
    self.assertEqual(self.test_region.chest_count, 0)
    assert(not self.test_region.is_accessible)
    assert(not bool(self.test_region.gates))
    assert(not self.test_region.is_clear)
    assert(not bool(self.test_region.items_found))

  def test_add_gate(self):
    dummy_gate = Gate(self.other_region, Requisite({"Test 1"}))
    self.test_region.add_gate(dummy_gate)
    assert(bool(self.test_region.gates))


















