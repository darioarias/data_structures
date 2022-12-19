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


if __name__ == "__main__":
    unittest.main(verbosity=2)
