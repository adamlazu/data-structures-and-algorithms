class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,item):
        if self.root == None:
            self.root = Node(item)
        else:
            self._insert(item, self.root)

    def _insert(self, item, curnod):
        if item < curnod.item:
            if curnod.left == None:
                curnod.left = Node(item)
            else:
                self._insert(item, curnod.left)
        
        elif item > curnod.item:
            if curnod.right == None:
                curnod.right = Node(item)
            else:
                self._insert(item, curnod.right)

    def preorder(self):
        if self.root == None:
            print('tree is empty')
        else:
            self._preorder(self.root)
    
    def _preorder(self, node):
        if node != None:
            print(node.item, end=' ')

            self._preorder(node.left)

            self._preorder(node.right)
    
    def inorder(self):
        if self.root == None:
            print('tree is empty')
        else:
            self._inorder(self.root)
    
    def _inorder(self, node):
        if node!= None:
            self._inorder(node.left)
            print(node.item, end=' ')
            self._inorder(node.right)

    def postorder(self):
        if self.root == None:
            print('tree is empty')
        else:
            self._postorder(self.root)
    
    def _postorder(self, node):
        if node!= None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.item, end=' ')

    def search(self, item):
        return self._search(self.head, item)

    def _search(self, curnod, item):
        if curnod == None:
            return 0

        if curnod.data == item:
            return 1
        elif curnod.data>item:
            return self._search(curnod.left,item)
        elif curnod.data<item:
            return self._search(curnod.right,item)
        

    