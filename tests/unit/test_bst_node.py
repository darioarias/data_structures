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

    def test_properties(self) -> None:
        n_one, *other_nodes = self.nodes
        one, *other_vals = self.vals

        self.assertEqual(
            n_one.val,
            one,
            "the value of this node was dynamically generated using a predetermined set thus the values should be equal",
        )
        self.assertEqual(
            n_one.val,
            one,
            'Since "val" is mapped to "value" the values should be the same',
        )

        self.assertIs(
            n_one.left,
            None,
            "when a node is initialized empty, this property should be None",
        )
        self.assertIs(
            n_one.right,
            None,
            "when a node is initialized empty, this property should be None",
        )

        n_two, n_three = other_nodes

        n_two.left = n_one
        self.assertFalse(
            n_two.left is None, "since we set the left property, it should not be none"
        )
        self.assertIs(
            n_two.left, n_one, "since we pointed left to one, left should be one"
        )

        n_two.right = n_three
        self.assertFalse(n_two.right is None, "right should now be pointing to n_three")
        self.assertIs(n_two.right, n_three, "right should now be pointing to n_three")

        self.assertIs(
            n_two.min,
            n_one,
            "this tree has vaues, 1, 2, 3. from two, the min value should be 1",
        )

        self.assertRaises(AttributeError, setattr, n_two, "min", Node(0))

        node_2 = Node(15)
        node = Node(10, right=node_2)
        self.assertIs(node.right, node_2)

        node.val = 10
        self.assertEqual(node.val, 10)
        self.assertEqual(node.val, node.value)

        node_4 = Node(50)
        node_5 = Node(150)
        node_3 = Node(100, left=node_4, right=node_5)

        self.assertIs(node_3.left, node_4)

    def test_operators(self) -> None:
        one, two, three = self.vals
        n_one, n_two, n_three = self.nodes

        self.assertLess(n_two, n_three)  # lt operator btw Node and Node
        self.assertFalse(n_three < n_two)  # lt operator btw Node and Node
        self.assertGreater(n_two, n_one)  # gt operator btw Node and Node
        self.assertFalse(n_one > n_two)  # gt operator btw Node and Node
        self.assertEqual(n_two, n_two)  # eq opeartor btw Node and Node
        self.assertNotEqual(n_two, n_one)  # eq operator btw Node and Node

        self.assertEqual(n_one, one)  # eq btw Node[int], int
        self.assertFalse(n_one == two)  # eq btw Node[int], int
        self.assertLess(n_two, three)  # lt btw Node[int], int
        self.assertFalse(n_two < one)  # lt btw Node[int], int
        self.assertGreater(n_two, one)  # gt btw Node[int], int
        self.assertFalse(n_two > three)  # gt btw Node[int], int

        self.assertIs(n_two.left, n_one)  # testing the 'is' operator
        self.assertIs(n_two.right, n_three)  # testing the 'is' operator

        n_str: Node[str] = Node("1")
        self.assertRaises(TypeError, operator.lt, n_str, n_one)
        self.assertRaises(TypeError, operator.gt, n_str, n_one)


if __name__ == "__main__":
    unittest.main(verbosity=2)
