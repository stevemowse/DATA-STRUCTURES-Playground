data = ((1, 2, None), 4, (5, 6, None))

class Treenode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(Treenode.height(self.left), Treenode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + Treenode.size(self.left) + Treenode.size(self.right)

    def inorder_transversal(self):
        if self is None:
            return []
        left = self.left.inorder_transversal() if self.left else []
        right = self.right.inorder_transversal() if self.right else []
        return left + [self.key] + right

    def preorder_transversal(self):
        if self is None:
            return []
        results = [self.key]
        results += Treenode.preorder_transversal(self.left) if self.left else []
        results += Treenode.preorder_transversal(self.right) if self.right else []
        return results

    def display(self, space="\t", factor=0):
        if self is None:
            print(factor * space + "0")
            return
        if self.left is None and self.right is None:
            print(space * factor + str(self.key))
            return
        Treenode.display(self.right, space, factor + 1)
        print(space * factor + str(self.key))
        Treenode.display(self.left, space, factor + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        left = self.left.to_tuple() if self.left else None
        right = self.right.to_tuple() if self.right else None
        return (left, self.key, right) if left or right else self.key

    @staticmethod
    def parse_tuple(data):
        if data is None:
            return None
        if isinstance(data, tuple):
            if len(data) == 3:
                node = Treenode(data[1])
                node.left = Treenode.parse_tuple(data[0])
                node.right = Treenode.parse_tuple(data[2])
            else:
                node = Treenode(data[0])
                node.left = Treenode.parse_tuple(data[1]) if len(data) > 1 else None
                node.right = Treenode.parse_tuple(data[2]) if len(data) > 2 else None
            return node
        else:
            return Treenode(data)
data = ((1, 2, None), 4, (5, 6, None))
# Test the corrected implementation
tree = Treenode.parse_tuple(data)
if tree is None:
    print("Failed to parse the tree. Check the input tuple structure.")
else:
    print("Tree as tuple:", tree.to_tuple())
    print("\nTree structure:")
    tree.display("     ")
    print("\nHeight:", tree.height())
    print("Size:", tree.size())
    print("Inorder traversal:", tree.inorder_transversal())
    print("Preorder traversal:", tree.preorder_transversal())