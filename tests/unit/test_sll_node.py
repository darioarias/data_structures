import unittest

from data_structures.nodes import SinglyLinkedListNode as Node


class TestSLLNode(unittest.TestCase):
    def setUp(self) -> None:
        self.vals = (1, 2, 3)
        self.nodes = (Node(val) for val in self.vals)

    def tearDown(self) -> None:
        del self.vals
        del self.nodes

    def test_properties(self) -> None:
        n_one, n_two, *_ = self.nodes
        one, *_ = self.vals

        self.assertEqual(n_one.value, one)
        self.assertEqual(n_one.val, one)
        self.assertIs(n_one.next, None)

        setattr(n_one, "value", 2)
        self.assertEqual(n_one.val, 2)
        n_one.val = 1
        self.assertEqual(n_one.val, 1)

        n_one.next = n_two
        self.assertIs(n_one.next, n_two)


if __name__ == "__main__":
    unittest.main(verbosity=2)
