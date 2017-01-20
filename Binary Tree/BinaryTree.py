class BinNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
    def isLeaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

class BinarySearchTree(object):
    def __init__(self, root = None):
        self.root = root
        self.string = str(self.root)
    def insert(self, data):
        if self.root is None:
            self.root = BinNode(data)
            self.string = str(self.root)
            return
        current = self.root
        previous = None
        switch = None
        while current:
            previous = current
            if current.data <= data:
                current = current.right
                switch = 1
            else:
                current = current.left
                switch = 0
        new_node = BinNode(data)
        if switch == 0:
            previous.left = new_node
        if switch == 1:
            previous.right = new_node
    def preorderPrint(self):
        if self.root:
            print(self.root)
        else:
            return
        BinarySearchTree(self.root.left).preorderPrint()
        BinarySearchTree(self.root.right).preorderPrint()
    def preorder__str__(self):
        self.string = str(self.root)
        if self.root is None:
            return ''
        self.string += '('+BinarySearchTree(self.root.left).preorder__str__()+')'
        self.string += '['+BinarySearchTree(self.root.right).preorder__str__()+']'
        return self.string
    def inorderPrint(self):
        if self.root is None:
            return
        BinarySearchTree(self.root.left).inorderPrint()
        print(self.root)
        BinarySearchTree(self.root.right).inorderPrint()
    def inorder__str__(self):
        self.string = str(self.root)
        if self.root is None:
            return ''
        self.string = '('+BinarySearchTree(self.root.left).inorder__str__()+')'+self.string
        self.string += '['+BinarySearchTree(self.root.right).inorder__str__()+']'
        return self.string
    def postorderPrint(self):
        if self.root is None:
            return
        BinarySearchTree(self.root.left).postorderPrint()
        BinarySearchTree(self.root.right).postorderPrint()
        print(self.root)
    def postorder__str__(self):
        self.string = str(self.root)
        if self.root is None:
            return ''
        self.string = '['+BinarySearchTree(self.root.right).postorder__str__()+']'+self.string
        self.string = '('+BinarySearchTree(self.root.left).postorder__str__()+')'+self.string
        return self.string
    def search(self, data):
        if self.root is None:
            return False
        if data < self.root.data:
            return BinarySearchTree(self.root.left).search(data)
        elif data > self.root.data:
            return BinarySearchTree(self.root.right).search(data)
        else:
            return True
    def min(self):
        if self.root is None:
            raise ValueError('Error: Tree is empty')
        if self.root.left is None:
            return self.root.data
        return BinarySearchTree(self.root.left).min()
    def max(self):
        if self.root is None:
            raise ValueError('Error: Tree is empty')
        if self.root.right is None:
            return self.root.data
        return BinarySearchTree(self.root.right).max()
    def height(self):
        if self.root is None:
            return -1
        def max(x, y):
            if x >= y:
                return x
            else:
                return y
        return max(BinarySearchTree(self.root.left).height(),
                   BinarySearchTree(self.root.right).height()) + 1
    def levelorderPrint(self):
        nodes = [self.root]
        while len(nodes) != 0:
            print(nodes[0])
            if nodes[0].left:
                nodes.append(nodes[0].left)
            if nodes[0].right:
                nodes.append(nodes[0].right)
            del nodes[0]
    def delete(self, data):
        def deleteUtil(tree, data, parent, switch):
            # parameter parent records reference to parent node
            # parameter switch = 0 if current node is left of parent node
            if tree.root is None:
                return
            if tree.root.data != data:
                if data <= tree.root.data:
                    # go to search left subtree
                    deleteUtil(BinarySearchTree(tree.root.left), data, tree.root, 0)
                else:
                    # go to search right subtree
                    deleteUtil(BinarySearchTree(tree.root.right), data, tree.root, 1)
            else:
                if tree.root.isLeaf():
                    # target node is a leaf, directly delete it
                    if switch == 0:
                        parent.left = None
                        return
                    else:
                        parent.right = None
                        return
                elif tree.root.left is None:
                    # target node only has right subtree
                    # replace target node with root of right subtree
                    ref = tree.root.right
                    if switch == 0:
                        parent.left = ref
                        return
                    else:
                        parent.right = ref
                        return
                elif tree.root.right is None:
                    # target node only has left subtree
                    # replace target node with root of left subtree
                    ref = tree.root.left
                    if switch == 0:
                        parent.left = ref
                        return
                    else:
                        parent.right = ref
                        return
                else:
                    # target node has both left and right subtrees
                    # Find min value node of right subtree
                    def getMin(tree, parent):
                        if tree.root.left is None:
                            return [tree.root, parent]
                        else:
                            return getMin(BinarySearchTree(tree.root.left), tree.root)
                    temp = getMin(BinarySearchTree(tree.root.right), tree.root)
                    minNode = temp[0]
                    minParent = temp[1]
                    # Remove minNode from the tree and adjust links
                    minParent.left = minNode.right
                    # Replace target node with minNode and adjust links
                    minNode.left = tree.root.left
                    minNode.right = tree.root.right
                    if switch == 0:
                        parent.left = minNode
                        return
                    else:
                        parent.right = minNode
                        return
        deleteUtil(self, data, None, None)
