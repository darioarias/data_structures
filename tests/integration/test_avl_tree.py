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


if __name__ == "__main__":
    unittest.main(verbosity=2)
