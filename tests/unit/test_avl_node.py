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

    def test_properties(self) -> None:
        n_two, n_one, n_three = self.nodes
        two, *_ = self.vals

        self.assertEqual(n_two.value, two)
        n_two.value = 20
        self.assertEqual(n_two.value, 20)
        self.assertEqual(n_two.val, 20)

        self.assertIs(n_two.left, None)
        self.assertIs(n_two.right, None)
        self.assertEqual(n_two.height, 0)

        self.assertIs(n_two.min, n_two)
        self.assertEqual(n_two.left_height, -1)
        self.assertEqual(n_two.right_height, -1)
        self.assertEqual(n_two.balance_factor, 0)

        n_two.left = n_one
        self.assertIs(n_two.left, n_one)
        self.assertIs(n_two.min, n_one)
        self.assertEqual(n_two.balance_factor, 1)
        self.assertEqual(n_two.left_height, 0)
        self.assertEqual(n_two.right_height, -1)

        n_two.right = n_three
        self.assertIs(n_two.right, n_three)
        self.assertIs(n_two.min, n_one)
        self.assertEqual(n_two.balance_factor, 0)
        self.assertEqual(n_two.right_height, 0)

        # props integrity
        self.assertRaises(AttributeError, setattr, n_two, "min", Node(10))
        self.assertRaises(AttributeError, setattr, n_two, "right_height", 1)
        self.assertRaises(AttributeError, setattr, n_two, "left_height", 0)
        self.assertRaises(AttributeError, setattr, n_two, "balance_factor", -1)

    def test_operators(self) -> None:
        n_two, _, n_three = self.nodes
        two, one, three = self.vals

        self.assertEqual(n_two, two)
        self.assertEqual(n_two, Node(2))

        self.assertGreater(n_two, one)
        self.assertGreater(n_two, Node(1))
        self.assertFalse(n_two > 10)

        self.assertLess(n_two, three)
        self.assertLess(n_two, n_three)
        self.assertFalse(n_two < 0)

        self.assertRaises(TypeError, operator.lt, n_two, "3")
        self.assertRaises(TypeError, operator.lt, n_two, Node("3"))

        self.assertRaises(TypeError, operator.gt, n_two, "1")
        self.assertRaises(TypeError, operator.gt, n_two, Node("1"))

    def test_iter(self) -> None:
        n_two, n_one, n_three = self.nodes
        two, *_ = self.vals

        val, left, right = n_two

        self.assertIs(left, None)
        self.assertIs(right, None)
        self.assertEqual(val, two)

        n_two.left = n_one
        n_two.right = n_three

        _, left, right = n_two

        self.assertIs(left, n_one)
        self.assertIs(right, n_three)

    def test_repr_str(self) -> None:
        n_two, *_ = self.nodes
        two, *_ = self.vals

        self.assertEqual(str(n_two), str(two))

        class Node_(Node):
            pass

        temp = Node_(two)
        self.assertEqual(repr(temp), f"Node_({two!r})")


if __name__ == "__main__":
    unittest.main(verbosity=2)
