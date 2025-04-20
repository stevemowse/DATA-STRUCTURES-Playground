class Users:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class BSTtree:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = BSTtree(key, value)
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = BSTtree(key, value)
            else:
                self.right.insert(key, value)
        else:
            self.value = value
        return self

    def find(self, key):
        if self is None:
            return None 
        if key == self.key:
            return self.value
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.find(key)

    def update(self, key, value):
        if self is None:
            return BSTtree(key, value)
        if key == self.key:
            self.value = value
        if key < self.key:
            if self.left is None:
                self.left = BSTtree(key, value)
            else:
                self.left.update(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = BSTtree(key, value)
            else:
                self.right.update(key, value)
        return self
            
    def list_all(self):
        results = []
        if self is None:
            return []
        if self.left is not None:
            results += self.left.list_all()
        results.append(self.key)
        if self.right is not None:
            results += self.right.list_all()
        return results

    def display(self, space="\t", level=0):
        if self is None:
            print(space * level + "∅")
            return
        
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
            
        self.right.display(space, level + 1)
        print(space * level + str(self.key))
        self.left.display(space, level)

# Create user objects
jaadhesh = Users("jaadhesh", "Jadhesh", "jaadhesh@example.com")
aakash = Users("aakash", "Aakash", "aakash@example.com")
biraj = Users("biraj", "Biraj", "biraj@example.com")
haemaeth = Users("haemaeth", "Haemaeth", "haemaeth@example.com")
sonaksh = Users("sonaksh", "Sonaksh", "sonaksh@example.com")
sidhat = Users("sidhat", "Sidhat", "sidhat@example.com")

# Create and populate BST
bsttree = BSTtree(jaadhesh.username, jaadhesh)
bsttree.insert(aakash.username, aakash)
bsttree.insert(biraj.username, biraj)
bsttree.insert(haemaeth.username, haemaeth)
bsttree.insert(sonaksh.username, sonaksh)
bsttree.insert(sidhat.username, sidhat)

# Test find and update
print("sidhat:", bsttree.find(sidhat.username))
sidhat = Users("sidhat", "Sidhat Matako", "sidhat@gmail.com")
bsttree.update(sidhat.username, sidhat)
print("updated sidhat:", bsttree.find(sidhat.username))

# List all keys
print("All keys:", bsttree.list_all())

# Display tree
print("\nTree structure:")
bsttree.display("    ")