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

    def test_removing(self) -> None:
        tree = Tree(x for x in range(10))
        self.assertEqual(self.tree_len(tree), 10)

        tree.remove(8)
        tree.remove(7)

        assert tree.root is not None
        self.assertEqual(tree.root.right, 5)

        assert tree.root.right is not None
        self.assertEqual(tree.root.right.right, 9)

        tree_len = self.tree_len(tree)
        for num in range(12):
            found: bool = False
            if num in tree:
                found = True

            tree.remove(
                num
            )  # implicitly tests for when a value that doesn't exist is removed

            if found:
                self.assertEqual(self.tree_len(tree), tree_len - 1)
                tree_len -= 1

        self.assertIs(tree.root, None)
        self.assertEqual(self.tree_len(tree), 0)

        in_tree = [x for x in range(1, 10, 2)]
        out_of_tree = [x for x in range(2, 10, 2)]

        tree = Tree(in_tree)

        self.assertEqual(self.tree_len(tree), len(in_tree))

        for val, *_ in tree:
            self.assertFalse(val in out_of_tree)
            self.assertTrue(val in in_tree)

    def test_str(self) -> None:
        self.assertEqual(str(Tree([1, 2, 3])), str(Tree(x for x in range(1, 4))))
        self.assertEqual(
            str(Tree([1, 2, 3, 4, 5, 6])), str(Tree(x for x in range(1, 7)))
        )

    def test_static_methods(self) -> None:
        items = [x for x in range(12)]
        for val, *_ in Tree.from_list(items):
            self.assertIn(val, items)

        for val, *_ in Tree.from_iter(x for x in range(12)):
            self.assertIn(val, items)


if __name__ == "__main__":
    unittest.main(verbosity=2)
