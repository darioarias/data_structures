import operator
import unittest

from data_structures.adelson_velsky_landis import AVL as Tree
from data_structures.nodes import AVLTreeNode as TreeNode


class TestAVLTree(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def tree_len(self, tree: Tree) -> int:
        count: int = 0
        for _ in tree:
            count += 1
        return count

    def test_constructor(self) -> None:
        init_vals = (x for x in range(1, 10))
        tree = Tree(x for x in init_vals)

        for item in init_vals:
            self.assertIn(item, tree)

        for node in tree:
            self.assertIn(node.val, tree)
            self.assertIsInstance(node, TreeNode)

        init_list = [str(num) for num in range(1, 5)]
        tree = Tree(init_list)
        for value in tree:
            self.assertIn(str(value), init_list)

    def test_inserting(self) -> None:
        emp_tree = Tree()

        self.assertEqual(self.tree_len(emp_tree), 0)

        emp_tree.insert(10)
        self.assertEqual(self.tree_len(emp_tree), 1)

        assert emp_tree.root is not None
        self.assertIs(emp_tree.root.left, None)
        self.assertIs(emp_tree.root.right, None)

        emp_tree.insert(11)
        emp_tree.insert(12)

        self.assertEqual(emp_tree.root.val, 11)
        self.assertEqual(emp_tree.root.left, 10)
        self.assertEqual(emp_tree.root.right, 12)
        self.assertEqual(self.tree_len(emp_tree), 3)

        reverse_queue = [9, 6, 4, 8, 5, 2, 0, 7, 1, 3]
        for val, *_ in Tree(x for x in range(10)):
            self.assertEqual(val, reverse_queue.pop())


if __name__ == "__main__":
    unittest.main(verbosity=2)
