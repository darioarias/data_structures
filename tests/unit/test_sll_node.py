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

    def test_operators(self) -> None:
        *_, n_three = self.nodes
        *_, three = self.vals

        self.assertEqual(n_three, Node(3))
        self.assertEqual(n_three, three)
        self.assertFalse(n_three == 2)

    def test_iter(self) -> None:
        n_one, n_two, *_ = self.nodes
        one, *_ = self.vals

        val, next_ = n_one

        self.assertEqual(val, one)
        self.assertIs(next_, None)

        n_one.next = n_two

        _, next_ = n_one
        self.assertIs(next_, n_two)

    def test_structure(self) -> None:
        n_one, *_ = self.nodes

        self.assertIsInstance(n_one, tuple)
        self.assertIsInstance(n_one, Node)

    def test_repr_str(self) -> None:
        n_one, *_ = self.nodes
        one, *_ = self.vals

        self.assertEqual(str(n_one), str(one))

        class Node_(Node):
            pass

        n = Node_(one)

        self.assertEqual(repr(n), f"Node_({one!r})")
        self.assertEqual(
            "1 -> 2 -> 3",
            " -> ".join(str(node) for node in (Node(1), Node(2), Node(3))),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
