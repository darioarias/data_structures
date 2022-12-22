# Data Structures

## Available in data_structures
### Nodes
* You will find a generic the `BinarySearchTreeNode` class
  * Use this to annotate your code and to understand how the data can be linked in memeory (via reference, etc)
* You will find generic the `AVLTreeNode` class
  * likewise, use this to annotate your code and to understand how data can be linked in memory 
You can also use these classes to play around and build your own data structure. 

### Data Structures
* You will find an `AVL` implementation, which uses `AVLTreeNode` under the hood. 
  * This class can be printed.

  ```
  # for example
  print(AVL(x for x in range(12))) 

  # The following will be printed
  #     ┌─11
  #   ┌─10
  #   │ └─None
  # ┌─9
  # │ └─8
  # 7
  # │   ┌─6
  # │ ┌─5
  # │ │ └─4
  # └─3
  #   │ ┌─2
  #   └─1
  #     └─0

  ```

* You will also find an implementation for `BinarySearchTree`
  * can also be printed liked `AVL`

* You will find implementations for both, `SinglyLinkedList` and `DoublyLinkedList` 
  * Both of these can be printed
  ```
  # for example
  
  print(SinglyLinkedList(x for x in range(1, 5)))
  # prints: 1 -> 2 -> 3 -> 4

  print(DoublyLinkedList(x for x in range(1, 5)))
  # prints: 1 <-> 2 <-> 3 <-> 4
  ```
* You will find an implementation for `Heap`
  * `Heaps` can either be min or max and only handle basic data types

* You will find an implementation for `PriorityQueue`
  * `PriorityQueue` can handle complex and abstract data types if a key function is provided
## About the code
The code provided here is not meant to solve any problem for you. It is meant to give you the tools to understand and play around with different solutions for programming problems. 


For example, given a problem like, [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/), I can use an input list such as `[2,1,3]` and construct a BST on my local environment and play around with it.
```
from data_structures import BinarySearchTree as Tree
from data_structures.nodes import BinarySearchTreeNode as Node

root = Tree.from_mapped_list([2,1,3]).root
def is_valid_BST(root: Node):
    ...
is_valid_BST(root)
```
after this, I can use my debugging tool to see how the `is_valid_BST` algorithm work. Moreover, I can play around with different inputs to test my assumptions. 
