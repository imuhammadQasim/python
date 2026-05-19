class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
        
class BST:
    def __init__(self):
        self.root = None

    def insertData(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            print(f"Inserted {value} as the Root Node.")
            return
            
        current = self.root
        while True:
            if value < current.value: 
                if current.left is None:
                    current.left = new_node
                    print(f"Inserted {value} to the left of {current.value}.")
                    return 
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    print(f"Inserted {value} to the right of {current.value}.")
                    return 
                current = current.right

    
    def search(self, target):
        current = self.root
        while current is not None:
            if target == current.value:
                print(f" Target found in the {current.value}")
                return True
            
            elif target < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left 
        return current.value
    
    def find_max(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
            
# --- Execution ---
tree = BST()
tree.insertData(10)
tree.insertData(5)
tree.insertData(15)
tree.insertData(7)
tree.insertData(8)
tree.insertData(1)

print(tree.search(8))
print(tree.find_min())
print(tree.find_max())