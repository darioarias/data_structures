import operator
import unittest

from data_structures.nodes import BinarySearchTreeNode as Node


class TestBSTNode(unittest.TestCase):
    def setUp(self) -> None:
        self.vals = (1, 2, 3)
        self.nodes = (Node(val) for val in self.vals)

    def tearDown(self) -> None:
        del self.vals
        del self.nodes


if __name__ == "__main__":
    unittest.main(verbosity=2)
