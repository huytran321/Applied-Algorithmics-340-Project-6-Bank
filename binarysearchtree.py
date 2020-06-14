class Node:
    def __init__(self, key, value = None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, theNode):
        self.__leftChild = theNode

    def setRightChild(self, theNode):
        self.__rightChild = theNode

    def getKey(self):
        return self.__key

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild == None

    def __str__(self):
        return str(self.__key) + " " + str(self.__value)

    def __repr__(self):
        return str(self.__key) + " " + str(self.__value) 

class BinarySearchTree:
    def __init__(self):
        self.__size = 0
        self.__root = None

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def get(self, key):
        if self.__root == None:
            return None
        if self.__root.getKey() == key:
            return self.__root.getValue()
        currentNode = Node(8)
        currentNode = self.__root
        while currentNode != None and currentNode.getKey() != key:
            if currentNode.getKey() > key:
                  currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        if currentNode == None:
            return None
        else:
            return currentNode.getValue()

    def __getitem__(self, key):
        return self.get(key)

    def insert(self, key, value):
        if self.__root == None:
            self.__root = Node(key, value)
            self.__size = 1
            return
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() == None:
                    newNode = Node(key, value)
                    currentNode.setLeftChild(newNode)
                    self.__size += 1
                    return
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    newNode = Node(key, value)
                    currentNode.setRightChild(newNode)
                    self.__size += 1
                    return
                else:
                    currentNode = currentNode.getRightChild()

    def __setitem__(self, key, value):
        self.insert(key, value)

    def inOrderTraversal(self, func):
        theNode = self.__root
        self.inOrderTraversalRec(self.__root, func)

    def inOrderTraversalRec(self, theNode, func):
        if theNode != None:
            self.inOrderTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getKey(), theNode.getValue())
            self.inOrderTraversalRec(theNode.getRightChild(), func)


    def remove(self, key):
        if self.__root == None:
            return False
        # This block of code deals with the root node being removed
        if self.__root.getKey() == key:
            if self.__root.isLeaf():
                self.__root == None
            elif self.__root.getRightChild() == None:
                self.__root = self.__root.getLeftChild()
            elif self.__root.getLeftChild() == None:
                self.__root = self.__getRightChild()
            else:
                replaceNode = self.__getAndRemoveRightSmall(self.__root)
                self.__root.setKey(replaceNode.getKey())
                self.__root.setValue(replaceNode.getValue())
        self.__size -= 1
        return True

    #Want currentNode pointer to point to partent of node to remove
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getLeftChild() and currentNode.getLeftChild().getKey() == key:
                foundNode = currentNode.getLeftChild()
                if foundNode.isLeaf():
                    currentNode.setLeftChild(None)
                elif foundNode.getLeftChild() == None:
                    currentNode.setLeftChild(foundNode.getRightChild())
                elif foundNode.getRightChild() == None:
                    currentNode.setLeftChild(foundNode.getLeftChild())
                else:
                    replaceNode = self.__getAndRemoveRightSmall(foundNode)
                    foundNode.setKey(replaceNode.getKey())
                    foundNode.setValue(replaceNode.getValue())
                self.__size -= 1
                break
            elif currentNode.getRightChild() and currentNode.getRightChild().getKey() == key:
                foundNode = currentNode.getRightChild()
                if foundNode.isLeaf():
                    currentNode.setRightChild(None)
                elif foundNode.getLeftChild() == None:
                    currentNode.setRightChild(foundNode.getLeftChild())
                elif foundNode.getRightChild() == None:
                    currentNode.setRightChild(foundNode.getRightChild())
                else:
                    replaceNode = self.__getAndRemoveRightSmall(foundNode)
                    foundNode.setKey(replaceNode.getKey())
                    foundNode.setValue(replaceNode.getValue())
                self.__size -= 1
                break
            else:
                if currentNode.getKey() > key:
                    currentNode = currentNode.getLeftChild()
                else:
                    currentNode = currentNode.getRightChild()
        return False

    def getAndRemoveRightSmall(self):
        pass

    def contains(self, key):
        if self.__root == None:
            return False
        elif self.__root.getKey() == key:
            return True
        currentNode = self.__root
        while currentNode != None and currentNode.getKey() != key:
            if currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        return currentNode != None

    def searchTree(self, key):
        return self.contains(self.__root, key)



