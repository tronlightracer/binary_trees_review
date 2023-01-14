from node import Node
from binary_tree import BinaryTree

# left = Node(5)
# head = Node(9)
# right = Node(13)

# head.left = left
# head.right = right

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(14))

if __name__ == '__main__':
    print(tree.head)
    print(tree.head.left)
    print(tree.head.right)
    print(tree.find(14))
