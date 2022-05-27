# Create a binary tree with nodes

class Node():
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        newNode = Node(value)
        runner = self.root

        if newNode.value < runner.value:
            if not runner.left:
                runner.left = newNode

            

    #     while runner:
    #         if newNode.value < runner.value:
    #             if runner.left == None:
    #                 runner.left = newNode
    #                 return self
    #             else:
    #                 runner = runner.left
    #         else:
    #             if runner.right == None:
    #                 runner.right = newNode
    #                 return self
    #             else:
    #                 runner = runner.right

myTree = Tree(7)

myTree.add(4)
# myTree.add(4).add(2).add(8)
print(myTree.root.left.value)
# myTree.add(4).add(2).add(8)
# print(myTree.root.left.value)