class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
    

class BST:
    def __init__(self):
        self.root = None
    
    # def insertData(self, data):
    #     new_node = Node(data)
    #     if self.root is None:
    #         self.root = new_node
    #         print(f"Inserted {data} as the Root Node.")
    #         return
    #     current = self.root
        
    #     while True:
    #         if data < current.value:
    #             if current.left is None:
    #                 current.left = new_node
    #                 print(f"Inserted {data} to the left of {current.value}.")
    #                 return
    #             current = current.left
    #         else:
    #             if current.right is None:
    #                 current.right = new_node
    #                 print(f"Inserted {data} to the right of {current.value}.")
    #                 return
    #             current = current.right


    def insertData(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        
        while True:
            if data < current.value:
                if current.left is None:
                    current.left = new_node
                    print(f"Inserted {data} to the left of {current.value}.")
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    print(f"Inserted {data} to the right of {current.value}.")
                    return
                current = current.right
      
    def search(self, target):
        if self.root is None:
            return None
        
        current = self.root
        
        while current is not None:
            if target == current.value:
                return True
            elif target < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def max(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.left is not None:
            current = current.right
        return current.value
    
    def min(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.right is not None:
            current = current.left
        return current.value

    
    # def inOrder(self, node):
    #     if node is not None:
    #         self.inOrder(node.left)
    #         print(node.value)
    #         self.inOrder(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.value)
            self.inOrder(node.right)
            
            
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.value)
            self.inOrder(node.right)
            
            
    def preOrder(self, node):
        if node is not None:
            print(node.value)
            self.preOrder(node.left)
            self.preOrder(node.right)
            
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value)
                
tree = BST()
data_list = [12, 3, 7, 18, 20]
for item in data_list:
    tree.insertData(item)

print("postOrder Travering start")
tree.postOrder(tree.root)