
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_rec(root.left, key)
        elif key > root.key:
            root.right = self._delete_rec(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_rec(root.right, temp.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, root, result):
        if root:
            self._inorder_rec(root.left, result)
            result.append(root.key)
            self._inorder_rec(root.right, result)
    def postorder(self):
        result = []
        self._postorder_rec(self.root, result)
        return result

    def _postorder_rec(self, node, result):
        if node:
            self._postorder_rec(node.left, result)
            self._postorder_rec(node.right, result)
            result.append(node.key)

    # ----------- Count total nodes -----------
    def count_nodes(self):
        return self._count_nodes_rec(self.root)

    def _count_nodes_rec(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_rec(node.left) + self._count_nodes_rec(node.right)

# Example usage
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("Inorder traversal:", bst.inorder())
print("Postorder traversal:", bst.postorder())

print("Search 40:", bst.search(40))  
print("Search 90:", bst.search(90))  

bst.delete(20)
print("Inorder after deleting 20:", bst.inorder())
print("Postorder after deleting 20:", bst.postorder())


print("Total entries:", bst.count_nodes())

