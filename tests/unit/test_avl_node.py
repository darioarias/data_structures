import operator
import unittest

from data_structures.nodes import AVLTreeNode as Node


class TestAVLNode(unittest.TestCase):
    def setUp(self) -> None:
        self.vals = (2, 1, 3)
        self.nodes = (Node(val) for val in self.vals)

    def tearDown(self) -> None:
        del self.vals
        del self.nodes


if __name__ == "__main__":
    unittest.main(verbosity=2)
