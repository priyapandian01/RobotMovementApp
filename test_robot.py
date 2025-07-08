# test_simulator.py

import unittest
from simulator import MovementEngine

class TestBotMovement(unittest.TestCase):
    def setUp(self):
        self.engine = MovementEngine()
        self.engine.register_bot("Alpha")
        self.engine.register_bot("Beta")

    def test_initial_positions(self):
        self.assertEqual(self.engine.locate_bot("Alpha"), (0, 0))
        self.assertEqual(self.engine.locate_bot("Beta"), (0, 0))

    def test_move_east(self):
        self.engine.send_instruction("Alpha", "E2")
        self.assertEqual(self.engine.locate_bot("Alpha"), (2, 0))

    def test_prevent_overlap(self):
        self.engine.send_instruction("Alpha", "E3")
        self.engine.send_instruction("Beta", "E5")
        self.assertEqual(self.engine.locate_bot("Beta"), (2, 0))

    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            self.engine.send_instruction("Alpha", "Z5")

    def test_unknown_bot(self):
        with self.assertRaises(ValueError):
            self.engine.send_instruction("Ghost", "E2")

if __name__ == "__main__":
    unittest.main()
