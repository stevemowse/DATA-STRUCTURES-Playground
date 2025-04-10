#we will have a treenode which will alow user,username,email
#we will reprsent and str in the username
#we will have to know how to enter and edit a function in the treemode
#we will have make a bst
#a bst tree is where the left is lesser than the right each time it is inserted 
#we will have to find the value,upadate and list all
#we will look for the nodes if itis greater we move to the left
#if it is esser we move tothe right
#we will then have to update the nodes
#we will then have to list all
class Users:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
    def __repr__(self):
        return "username={},name={},email={}".format(self.username,self.name,self.email)
    def __str__(self):
        return "username={},name={},email={}".format(self.username,self.name,self.email)
    #we will have a function that will allow greatings and allow insertation of a greating
    def greatings(self,name):
        return "hey {} my name is{} is this your name ?{} and is this is youremail={}".format(name,self.name,self.username,self.email)
#we hae to enter the loop
#a tree node is a data structure which storesto the left and right
#First lets look at the class user database
class Userdatabase:
    def __init__(self):
        #we willl store the self.users in a list
        self.users=[]
    #we will have an insert function that will be used to insert into the self.users
    #we will insert the username then user
    def insert(self,username,user):
        pass
    #we will find using the username
    #we will return the username
    def find(self,username):
        pass
    #we will then update by passing the find because we looked dirrectly from the list
    #we will insert the username then insert the user
    def update(self,username,user):
        pass
    #we willthen list evreything from the list
    def list_all(self):
        pass
#the user database  insert is of o(n)time complexity and 0(1)space complexity as they increase with output
#the user database find is of 0(n) time complexityas it increases while it searches the more the values
#the update is of 0(n) time complexity and 0(n) space complexity as they insert directly to a place
#we will have a tree node that will be used to parse the tuple
#this is a function that will contain the data that willbe used to parse through the tuple
#when parsing a the tuple functions we need to have the data in the double brackets

data=(((1,2,None),4,(5,6,None)))
class Treenode:
    #the function will allow key values
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    #this function willconfirm and parse the tuple to the left and right node
    #the function will be a static method meaning ot will only allow in values that are instand
    #we will have a height and size function
    def height(self):#we only use the self because it is a static method
        pass
    def size(self):
        pass
    #we will look forthe inrder transeversal
    def inorder_transversal(self):
        pass
    #we willalso have a prorder transversal
    def preorder_transversal(self):
        pass
    #we will also have a display we willonly use the self because it is a static method
    def display(self,space="\t",factor=0):
        pass
    #this is a function that will convert back to a tuple
    #this is a rverse
    def to_tuple(self):
        pass
    @staticmethod
    #the self is never used in the static method because the static method does not parse the self
    #the static method acts as a self inbuilt function ofthe instance hence does not acces the self
    def parse_tuple(data):
        pass
#we insert the data intothe treenode which has a static method
tree=Treenode(data)
tree.to_tuple()
tree.display(" ")
print(tree.height())
print(tree.size())
print(tree.inorder_transversal())
print(tree.preorder_transversal())
#we will have a bst tree
#a bst tree isa self balancingf tree
class BSTtree:
    #we will alow an optional parsing ofnthe value functions
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
    #we will allow insertation
    def insert(self,key,value):
        pass
    #we will allow finding
    def find(self,key):
        pass
    #we will allow for updating of the treenode
    def update(self,key,value):
        pass
    #we will allow for listing all in an inorder transversal type
    def list_all(self):
        pass
tree=BSTtree
class AVLTee:
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
    #we will have to get the height
    def _get_height(self):
        pass
    #we will get the balance of the right and left node
    def _get_balance(self):
        pass
    #we will the have to rotate right and left
    def _rotate_right(self,y):
        pass
    def _rotate_left(self,x):
        pass
    #we will hev to insert and balance
    #we set the value to be equal to none incase we do not  insert the values
    def insert(self,key,value=None):
        pass
    #we will checkif the key matches the key inside
    #because this is somehow like a bst we  check if the kjey matches the key inside
    def find(self,key):
        pass
    #we will then have to update
    #we will chck if the key macheches the key and then update the value
    def update(self,key,value):
        pass
    #we will then list every thing in inordertransversal
    def list_all(self):
        pass
#We will then have check if the are bst
def isbst(node):
    pass

