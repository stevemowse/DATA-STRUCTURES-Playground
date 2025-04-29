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
aakash=Users("aakash","akashmavi","aakash@gmail.com")
#we acces using the aakash from theoutside because the aaksah already repressents the while structure
jaadhesh=Users("jadhesh","jadheshmavi","jadhesh@gmail.com")
biraj=Users("biraj","birajmavi","biraj@gmail.com")
sidhat=Users("sidhat","sidhatmavi","sidhat@gmail.com")
sonaksh=Users("sonaksh","sonakshmavi","sonaksh@gmail.com")
haemaeth=Users("haemeth","haemethmavi","haemeth@gmail.com")

aakash.greatings("jane")

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
        #we will initially have an initial position
        #the insert inserts at the given index while apend adds at the end  of a position
        #we need to insert at given indexes
        #before entering a while loopwe will always have an index
        #the i=0is the begining of the list
        i=0
        #the i should be before thelenghth of the self.users
        #the less than instead of less than and equal to elliminates the  the last index  while <=includes the last index
        #because we are comparimg two it is efficient
        #because we are looking for a single value the<= is efficient
        #when duplicate the new user will be inserted after the original this makes the hash mapbetter for indexing
        while i<len(self.users)-1:
            #we want to increament the i byone so we will break
            if user.username<self.users[i].username:
                #we will not increament if it is lesser
                break
            #we will increament by one
            i+=1
        #we will then insertat the first index which is index i
        self.users.insert(i,user)
    #find using the username
    #we will return the username
    def find(self,username):
        #we will have  to find the username in the self.users
        #these generalise and put evrything as an individual in the neme user
        for user in self.users:
            #if the user .username matches tehj incoming
            if user.username==username:
                #we return the whole user
                return user
    #we will then update by passing the find because we looked dirrectly from the list
    #we will insert the username then insert the user
    #the user being pased is  used to find the  username of that user meaning we are updating the user
    #because we are updating the user we dfo not need the username
    def update(self,user):
        #we will pass in the find into the target
        target=self.find(user.username)
        #we use  the userbecause the self does not contain the name and the email
        #the whole user contains the functions listed
        target.name,target.email=user.name,user.email
    #we willthen list evreything from the list
    
    def list_all(self):
        #we will return everything in the self.users
        #we will list directly because  it is not atree
        return (x for x in self.users if x)
        
#the user database  insert is of o(n)time complexity and 0(1)space complexity as they increase with output
#the user database find is of 0(n) time complexityas it increases while it searches the more the values
#the update is of 0(n) time complexity and 0(n) space complexity as they insert directly to a place
#we will have a tree node that will be used to parse the tuple
#this is a function that will contain the data that willbe used to parse through the tuple
#when parsing a the tuple functions we need to have the data in the double brackets
#we will give the jadhesh a value function
jadhesh=Users("jadhesh","jadheshmose","jadheshmose@gmail.com")
userdatabase=Userdatabase()
userdatabase.insert(aakash.username,aakash,)
userdatabase.insert(biraj.username,biraj)
userdatabase.insert(haemaeth.username,haemaeth)
userdatabase.insert(sonaksh.username,sonaksh)
userdatabase.insert(sidhat.username,sidhat)
userdatabase.insert(jaadhesh.username,jaadhesh)
userdatabase.find(jaadhesh)
#this is used to look for the find then updates the value after finding
userdatabase.update(jaadhesh)
userdatabase.list_all()
#we must alwayshave double bracets which will be used to modify the data
#interprating the treenode structure with real world experience
#we have areal tree of which has roots  if the tree doesnthave roots then it cant continue growing
#if the left and right nodes whch we need to be a layer on each other
#we need the tree return a node wich means it is a layer of onther
#we then return the treenode if it doesnt have branches we return evemif it has one value or a none

#converting to tuple we have to check for  if the left and right is a none
#this is like checking for the main root node where the root originates from and then printing the node
#we then have have to check for the left and right and then return by adding  throughn out'
#geting the 
#
data=(((1,2,None),4,(5,6,None)))
class Treenode:
    #the function will allow key values
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        #this sets the initial height of a node to be a 1 if the left and right are nones
        #.height=1
    #this function willconfirm and parse the tuple to the left and right node
    #the function will be a static method meaning ot will only allow in values that are instand
    #we will have a height and size function
    def height(self):#we only use the self because it is a static method
        #we use the node for updates
        if self is None:
            return 0
        #we use the 
        return 1+max(Treenode.height(self.left),Treenode.height(self.right))
    #the size is used to call the totallnumber of nodes in the avl tree
    def size(self):
        #we will use the node because it is updatable
        if self is None:
            return 0
        return 1+Treenode.size(self.left)+Treenode.size(self.right)
    #we will now have to get a balnce
    #we will look forthe inrder transeversal
    def inorder_transversal(self):
        #we need to return the emt if the self is a none
        if self is None:
            return []
        #we then give the left and the right value function
        #because it is a none type it means there is no value in the self.left hence we have to check
        #we should not put a none while accesing a list hence may lead to a none opranda cces
        left=self.left.inorder_transversal() if self.left else []
        #we check forthe left and then the right
        #we will have 
        right=self.right.inorder_transversal() if self.right else []#the error occured because we put the none in the list hence leeding toa none operand in the list
        #commas returns nested tuples instead of directedlists
        
        return left+[self.key]+right
    def preorder_transversal(self):
        #we will check if theself is a none because the compiller returns a none type object
        if self is None:
            return []
        #in the preorder transversale put the key inide the results
        #this is because the key come first then the left and then theright 
        #compared to the inorder transversalwhere the root is started first we apend when we start from the root
        #first we have to have an initial result function
        results=[self.key]
        #we wil insert into the resultsthe key first because we are starting with the key
        #we will add the key into the results because we want to atrt withthe key
        results+=Treenode.preorder_transversal(self.left)
        #we will thej ad tothe right indexes
        results+=Treenode.preorder_transversal(self.right)
        
        return results
        
    def display(self,space="\t",factor=0):
        #we will first print a zero if there is nothing to show off
        if self is None:
            #this maintains the  tree structure untill we reach at the none point
            print(factor*space+"0")
            return
            #because we are returning single digi
        #we will check if the left and right is a none so we print a key
        #we are checking the leftand right functions directly and hence we are not checking the key but checking the inside function
        if self.left is None and self.right is None:
            #we convert the self .key tostr inordertoallow for str and both numbers because even numbers can be turned back to str
            print(space*factor+str(self.key))
            #ingle digits during spacing
        #compared to the plus =1 which we will return multiple digits at a time
        #ths +=is mainly use inbinary trees
        #the +1 does not modify the orriginal variables compared to the +=1 which modifys the orriginal variable 
        #ina a binary searchg we start with the zero and modify it till we get the osition of the card
        #here we just return the value of the factor without modifying them
        #we use only one digit thets why we return
        #the return allows reccursive calls from the downwards
        #by convertimg to tupl we look at the left and right of the tree in order to reverse
        #we start from the bottom
        #we then use a comma to add everythig from the left and right
        #WHEN converting to an inorder transversal
        #we have to return a list of things
        #using the tree format we start from the child lef then node then riht
        #we will check in a reccursive order from the left and right 
        #we will then give the two variable functions
        #we will then  have to append the results wherre we add the key
        #as a tree we look  for the left and right and add the key in the midle
        #in preorder transversal we check for the  key first then look for the left then right 
        #we will stert with the key then left right
        #as a tree we start from the stem ofthe root looking left and right
        
            return 
        #then weuse the display right first because the human brain displays like thet incontrary to the too tuple which is used only to acces
        Treenode.display(self.right,space,factor+1)
        print(space*factor+str(self.key)) 
        Treenode.display(self.left,space,factor+1)      
        #this is a function that isused to display how we view the values in the pa
    #this is a function that will convert back to a tuple
    #this is a rverse
    #this is a function that is used to return the tuple back to its orriginall self
    def to_tuple(self):
        #we will return a none if the self is a none
        if self is None:
            return None
        #we will now have to checkmfor the left or the right
        #we willcheck for it as a block because  we are  reversingb the tuple
        if self.left is None and self.right is None:
            return self.key#this return the key directly if the left and right of the values are a none
        #this is a function that will be used 
        #wwe have to do the function reccursively
        #we will reccursively callthe left subvltre
        # #this calls the right side reccursively
        #this converts everythingg on the eft back to the tule
        #the if else means if there is a left else to return a none
                #this converts verything to the right to tuyple
        #this also checks if the left or the right is not a none
        #thisreturns the left and right together plaus the ey first
        #we atrt with the left to right because of the stardd python and soas to return the structure in the same way
        #this is comtarary to the displaywhere we start with the right then the left of which is almost the way the human breain interprates thing ie when we write in a piece of paper
        return Treenode.to_tuple(self.left),self.key,Treenode.to_tuple(self.right)
    #we use a comma during turning to tuplebecause  we want to preserve the structure compared 
    #compared to the transversals which we want to return the lst directly hence adding the left and right from the left and right
        
    @staticmethod
    #the self is never used in the static method because the static method does not parse the self
    #the static method acts as a self inbuilt function ofthe instance hence does not acces the self
    def parse_tuple(data):
        #we will first check if th data is anone and return a none whenthi
        #this is efficient during searching for a tree hence we will return a none when any of the data values are a none
        #this is good in maintainig the tree structure'
    
    #thisis why we check if the left is a none and make them to be treenodekeya nd value
    #during insertation in a bst
    #this ensures that  the treenodestructure i returned back toits originall
    #when checking if the left is a none we return the treenode in order to search reccursively
    #because this is a tuple will just check if the data is a none direcly
    #thisensures that the structure of the treenode is maintained
        if data is None:
            return None
        #the parsetuple is used as an insert method
        #we will confirm the tule
        #if the data is a none then we return a none
        #this marks the end of the reccursio
        if isinstance(data,tuple) and len(data)==3:
            #we will then have to gie the nodes value functions
            #we pass the data at index one to be the key f thetree node
            node=Treenode(data[1])
            #we five the left and the right the data at the second and first index
            node.left=Treenode.parse_tuple(data[0])
            #we will then check for the right
            #we use the treenodenode twice because without using the treenode python wount find where to acces the parsetuple
            node.right=Treenode.parse_tuple(data[2])
           #we use the return node to buld a value because reccursion needs to return a value inorder tobuid a tree
           #we also need tocall the functions reccursively because they we already made and they were given the node values
            #because we assigned theeuals sig the nodeisable tobe called reccursively
            #compared to node=treenode data which ensures that the  data is given if it is one and terminates the rest if itisint
         
            #we will then check for the recursion
        #when the data is a none no more reccusive functions will be done and the node will be a none
        #we always first have to find the nod
        #we should return te node before perfomiing the reccursive call
        #we return the node before the tuple because  the else statement handles the case where the function is not a tuple
            return node
        else:
            #thisensures that there is reccursion
            #returning the treenode data 
            #the treenode ensures termination when we reach the end of the tuple
            #it also ensures that there is termination hence returns the lst treenode data
            #this also checks if thelen of data is 3
            #returning the trenode data ensures that the edge cases are covered
            #this directly returns the leaf nodes evenif the leatf nodes are a none
            #it also ensures that the data at the first place is returned when it is a single value the tree is returneddirectly
            return Treenode(data)
            
    #we could avboid thenode=treenode(data)which is used to check if the structure is of len1 and the left and right are not the same

#the static method only  ensures that the self is not reused the static method modifies the use of the selffunction insidethe class
#this function esures he tuple stuctures the isinstance function back to its originall by giveing the left and the right values ofthe treenode

tree=Treenode.parse_tuple(data)
#we wil;l create a node whixch is aways equal to yjeth
#thius coverts the tree pased to a tuple back to its original
#we print the treenode totupl and pass the tree
#we cannot put the data inside theto tuple because thedata is alreay inside thetreenode object
#the method is an instance itself and the function can only call using the already assed tuple
print("tuple",tree.to_tuple())
#we ahve to enter what we want tobe dsplayes
#the displaytree should always be displayed from the inside 
#the display function  is writen from the inside because the self is on the inside
tree.display("     ")
tree.height()
print(tree.size())
print(tree.inorder_transversal())
print(tree.preorder_transversal())
#we will have a bst tree
#a bst tree isa self balancingf tree
#we havbe a real tree where we will move downwards
#we move  wil have an insert where while inserting ifwe find the left is a none we put in the structure toreturn the whole tree structure
#we then insert at the end ofthe tree
#we will also have an update where we will check for the tree structure downwards as we want to change the structure
#we will then update where the structure matches the key
#moving the tree downwards will help locate where the tree has a problem
#we will also have to find where find is a return only and is not used to modify the tree hence we judt search the treee normaly
#we chek if the key matches the key given if not we move downwards and we do not alter with the structure ofthe tree
#we will then have a list all which we will move in an inorder transversal starting from the left,key then right
#we want to return  the intersections from down
#we will start with the list of results
#we will then heve to check for the intrersections from downwards util we reach upwards
#we will ass the left and right in a dood order starting with left and then right
#we will then append to the resultsthe keys because we are atrting from down we will have to append to the keys
#if it wat a pre order we start with the keys in the list bacause it will orderitself beacause we are starting from the root and then left and right

class BSTtree:
    #we will alow an optional parsing ofnthe value functions
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
    #we will allow insertation
    def insert(self,key,value):
        #we will chck toinsert to the left or right and check if the left is a none or has a value
        if key<self.key:
            #we will chec if the left is  a none because new nodes are alwaysinserted as leaf nodes
            #this is done to insert reccursively
            if self.left is None:
                #we call this inorder togo deeper
                #the self.left=bst tee value  makes the structure
                #compared to when assigning inserting we just ass direcly to the left
                #this prepares a stage for  insertation
                #we use the self.left=bsttree keyvalue for direct assignment of the left values
                
                self.left=BSTtree(key,value)#we after this insert at the left node 
            else:
                #we do notuse self.left= because the self.left updates imediately and puting self.left=makes it redundatnt
                self.left.insert(key,value)#this is used toreccurse deeper when searching
        #we check if the key is greater
        #we return the whole self value
        elif key>self.key:
            #we call the value reccursivelyand insert to the right
            #we check if the left is a none
            
            #we reccursivelycall the left
            if self.right is None:
                #we then call it reccursively to find an empty sport
                #in the treenode key value where we are looking to insert is where we will find the empty spot
                #we used the treenode functios instead ofthe bst tree of which the treenode only allows the keys only
                self.right=BSTtree(key,value)
                    #we will allow finding
            #else we insert to the  right of it
            else:
                #we insert directly to the right while it looks reccursively
                self.right.insert(key,value)#this is used to reccurse deeper when searching
            #else we update if the key exists we update the value
            #we update because we have slready inserted and we must insert either to the left and right
        else:
            #if they are not greater or lesser means they are equal
            self.value=value
            #we return the self toget back the structure but when finc=ding we do not need toget back the structure
        return self
    def find(self,key):
    #we will check if the self is anone so as to return a none while fi
        if self is None:
            return None 
        #we willcheck if the key mactches the keys in the self which id the mein otherwise we move tothe left or right
        if key==self.key:
            #we return the value
            return  self.value
        #if it is greater we move to the left or the right
        #we will use the  self.left.find because the fid does not allo the self inside instead huwa inajijazia
        if key<self.key:
            #we search to the left reccursively
            if self.left is None:
                #we will return the bst node tree making it to continue to go down
                return None
            else:
                return self.left.find(key)
        #we otherwise check if it is  more so we move to the right
        
        #we use the self.key because e are comparing directly to the key
        #we use an elif statement because it is a block state,ntand only one at a time is passed so we have to determne wheather to move to the left or move to the right
        elif key>self.key:
            #we search to the right as we wait for it to either return a none or return  the value
            #i was thinking the function could callto the right reccursively
            #whenever we are looking with the self we must use the left or right first
            #we ware using self.left .find because python fills for itself the  self function leaving the others
            #compared tothe node where python does not fill for itself
            #while using bsttree.find can be used the self.left .find is less verbous and readable
            if self.right is None:
                #we return the bst node tree to move downwars
                #we dont use the bsttree key value when finding because it will corrupt the data structure
                #we only return the value as the find is a search not a modifiier
                return None
            else:
                return self.right.find(key)
        #we return the self if we find nothing
        #after checking if it is greater or lesser we move to the left or right
        #we must first check for the key then move to the left and right        
    #we will allow for updating of the treenode
    #same as durimng insertation we musst checkif the self .left is none so as to insert to the left
    #we check if it is a none and update making it a bst and then  inserting to the left node
    #what if the the self .left is not a none
    #the functio will continue tosearch for the key more deeply
    #when we find the function we insertt 
    #this is the same while inserting we contiue searching downwards the tree
    #when we reach it is not a none we will then have  to  insert to the place where it is not a none
    #e reccursively call the root downwards the tree
    #we look for the stem downwards untill we find a place where the stemis not a none
    #we will then have to check forthe root downwards becaUSEIT IS A TREE
    #to make it a tree we have to returnmake the bst
    #when we reach downwards at the end we insert at the end of the tree
    #we will then insert at the bottom
    #adding to the left and right
    #this is the same as the  update we move the tree downwards 
    #we will then have to check when thekey matches theincoming key and then matches the value
    #we will checnge it to thevalue
    #compared to treansversing where we have topackthe keys
    #transversing we will have to check the left  and right amd print the node
    #this is like printing the intersection of the tree\
    #we will then have to apend while checkinhg in a reccursive order
    #we will use the plus sign because we are looking for the intersection
    #we will then have to check for the to tupe where we ill use a comma becaue wewantr every thing from the tree
    #we will then have to check for the preotrder transeveral
    #the preorder transversal we visit the root then the left subtree  is when we visit a tree from the left then the root then the right
    #the inorder transversal we will the  check for the left then the node then the right this follos a node order
    #in the inorder transversal we will apend thhe result
    #before appending we will then check  for the left and right as we add  then results .add self.key at the end
    #append means adding in an in order
    #we add the left and right the  add the key
    #that makes a inorder transversal
    #hence making the tree is being searchd from the bottom
    #we will  then have to check for the key first then add the left and then add the right
    #the key is then in the insside
    #interprating in real world
    #we will have to print out the intersection of the tree only which is a preorder transevreal hence the intersection is put in the list firs
    #we will have to check for the left thenright from the bottom of the tree and then use it tobe  appended to the tree
    #we will first check if the self .left is not nojne in order to append the result
    def update(self,key,value):
        #when updating we update acce to the left this is seen similar tothe ttoo tuple where we acces directly fromthe left
        #to maintain the structure
        if self is None:
            return BSTtree(key,value)
        #we will check  forthe matches
        #this is where the main key starts
        if key==self.key:
            #we will then update the value
            self.value=value
        #we will then move to the left then move to the right again
        #we will check if the self .left is a none inorder to make the tree structure and then reccurse deeper
        if key<self.key:
            #we insertreccursively
            if self.left is None:
                self.left=BSTtree(key,value)
            else:
            #when it is lesser  we insert to theleft  and update 
            #we use self.right .update to directlyupdate to the right
            #this meanswe reccursively caall tothe left
                self.left.update(key,value)
        #when greater then we reccursively callthe right
        #we check at the right keys
        elif key>self.key:
            #we return to the right reccursively
            #we update the right and insert at the right index when it i lesser
            if self.right is None:
                self.right= BSTtree(key,value)
            else:
                self.right.update(key,value)
    #using the self.left=bstree(key,value) opens up the room forinsertation  
    #we return self to allow chaining wherethe methods are knwn as one
    #we return the self because we have altered the structure of the tree
    
        return self
    #we alsoretiurn the wholese  
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    #we will allow for listing all in an inorder transversal type
    def list_all(self):
        #we will list all just the way we listated evry thing in the treenode
        #we will have a list of results
        results=[]
        #we will check if the self is a noe so as to return an emty list because we transversing
        if self is None:
            return []
        #we will then have  to check forthe left becaus e tisan inorder transversa we atart with the left then key then right
        #we use += because we do not want one value we want an increament of the the increament of values
        #we increament the ;eft and the right concurrently because we want to add to the keys inside
        #we will not write anything in then list all becasue this is not a node
        #we check if the self is a none inorder to list from the left then the right because the values are of a tree        if self.left is  None:
        #we chck the eft and rightto be none first reccursively and the print the keys so as to return the structure
        #we check if the self .left is not none so as not to pass tjrough the transversal reccursively
        if self.left is not None:
            #the +equal is used to bring up many valuesat once compared to the + which is only used to bring up one value
            results+=self.left.list_all()
        #we will then apend to the results
        
        results.append(self.key)
        #we will then add tyhe  right values
        
        #we will not write inside the list all because thid is not a node and the nodevalue was not given tobe written over
        #we check the n0one to stope theatribute errs
        #We will also check if the right is also a not none soas to not transverse through the tree and return the none type value
        if self.right is not None:
            results+=self.right.list_all()
        #we will also return the results which we have appended
        #what happensa if we do not return ressults
        #this means while we are adding the right and left the value might return a none
        #hence this meay results to type error
        #when we try to add the none on the left and right  thi will lead to a typee errorbecause we have a nomne function inside
        #this means that as we append the key we will not return the resultshence leeding to a none to the left and right leading totype error
        return results
    def display(self,space="\t",factor=0):
        #we will check for the none and print a zero
        if self is None:
            print(space*factor+"0")
            #we will have to return because w e are transversing upwards the tree and when transversing we need to  return because we are writing out individual by individual
            return
        #we will check for the self coming up the tree
        #checking for the left and roight is none prints only one value at once comapredto hen thereis a node return where the node is the whole structure of the tree
        #this will only return one value so we will have to modify
        if self.left is not None and self.right is not  None:
            print(factor*space+str(self.key))
            return
        #we will need to display from the right and print then left
        #this is an inorder like form of transversal thT we used to append
        #we will display the left values
        #we wount use self.left  or self.right is nonein an inorder trsnsversal because  it will destroy the rulesof the tree
        #if we check the left and right of the self it will only return a single value
        self.right.display(space,factor+1)
        print(space*factor+str(self.key))
        #they say assymtric is not needed to display the function hence we will not add+1 to the left
        self.left.display(self.left,space,factor)
        
        
#there was a problem during the comparisions
bsttree=BSTtree(jaadhesh.username,jadhesh)                                                                                                                                                      
#we willfirst insert the user name then the user value
#we use the username as key so that wecan compare
#wif we insert using without the aakash.username there will be no comparision
bsttree.insert(aakash.username,aakash)
bsttree.insert(biraj.username,biraj)
bsttree.insert(jaadhesh.username,jaadhesh)
bsttree.insert(haemaeth.username,haemaeth)
bsttree.insert(sonaksh.username,sonaksh)
bsttree.insert(sidhat.username,sidhat)
print("sidhat",bsttree.find(sidhat.username))
#thiswill update the username
sidhat=Users("sidhat","sidhatmatako","sidhat@gmail.com")
bsttree.update(sidhat.username,sidhat)
print("updatedsidhat",bsttree.find(sidhat.username))
print(bsttree.list_all())
bsttree.display("                ")
tree=BSTtree
#THE AVL TREE interprated in the real world situation
#we will have a tree but we will always have a height of one ofthe root because a tree always has a root or else it wil fall down
#the height will be used to compare and the balance will always be goten
#the balance  whichwillget the difference of the left and right root
#we will then have to get the rotations
#the right rotation means the rroot of the left and right moves to the  other side
#the left rotation means the tree move t the otherside
#this then makes the tree node face the other direction
#if it is the opposite then then we check rotate the other way by makingit straght and then make the mid to be the root by returning
#this is like tsrightening a tree then cjhanging the shape of the root if one root is greate than the other
#we ill then do the 
class AVLTee:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        #we will put an initial height of 1
        #the initial height is put to 1 because  at 1 when we have a none it will make it tobe a negative zero
        #also the height of a node is alwatys a 1 before making of its children to the left and right
        #the avl self.height tracks the height at the node
        self.height=1
    #we will have to get the height
    #we must also have a node
    #weuse the node because it is assed back when it is inserted
    #the get height above is used 
    def _get_height(self,node):
        #wewill have a node passed back
        #we will return directly the node .heightif else none
        #this was my main question on why we were updatingbthe height after inseting
        return node.height if node else None
    #we will get the balance of the right and left node
    #the node is kept there intimes
    def _get_balance(self,node):
        #we will subtract the nodes at the left and rigtht
           #we will the have to rotate right and left
        if node is None:
            return 0
        #we will then get the balance to the left and right
        #we includethe 1  to make sure that the root node is included
        return 1+(self._get_balance(node.left)-self._get_balance(node.right))
    def _rotate_right(self,y):
        x=y.left
        T2=x.right
        
        y.left=T2
        x.right=y
        
        #this is a function that is used to connect the height
        #this is a function that is used to update the height in the above 
        
        x.height=1+max(self._get_height(x.left),self._get_height(x.right))
        y.height=1+max(self._get_height(y.left),self._get_height(y.right))
        #we will then  use to  return the x the x is returned because it will be the new node after rotation
        #otherwise the function will loose the structure
        return x
    def _rotate_left(self,x):
        y=x.right
        T2=y.left
        
        x.right=T2
        y.left=x
        
        #we will then update the height after pointing
        x.height=1+max(self._get_height(x.left),self._get_height(x.right))
        y.height=1+max(self._get_height(y.left),self._get_height(y.right))
        #we will then return the y which will be the new root
        return y
    #we will hev to insert and balance
    #we set the value to be equal to none incase we do not  insert the values
    def insert(self,key,value=None):
        #wewill insert to the eft and right
        #we do not check the self.lef.keynbecause in the bst insertion we check the self.left and then check for the self.right insertation
        #the find alsoapplysthe same logic becaseif not found with the key we move to the left of the key and do the reccursive search
        #when we check directly  for the key because when it is greater we move to the leftand when it is lesser we checkin the right
        if key<self.key:#this means we have to insert to theleftnode
            #we then have to check if the self is a none inorder  to reccursively goto the left
            #we will check the self.left because  we want to insert to the left
            #we will check if it is not a none to avoid the none atribute error where we acces a none value
            #we will check if it is a none so as to make it atree
            if self.left is  None:
                #we make a recursive call to the left until we find an empty space
                #this is dne to check the empty space and make theinserted a node also
                self.left=AVLTee(key,value)
            #we will then look   to insert to the left 
            else:
                self.left.insert(key,value)
        elif key>self.key:
            #we check if the left is a none so that we insert and make it a tree node
            #if we do not do this we might corrupt the tree
            #we will also chek if it is not a none to avoid the none attribute error
            #we will check if it is a none so as to  put the left to be the tree node and insert
            #we check if it iss a none so as to insert into the leaf node and then make the whole self.right tobe a treende key andvalue
            
            if self.right is None:
                self.right=AVLTee(key,value)
            #we will then indert at the left
            else:
                #we check beforethe insertation so as to make it the treenode key value then put in to the left
                #this ensures that the tree is not corrupted
                self.right.insert(key,value)
        #we otherwise replace the value if it is not greTER THAN ORequal to
        #this is used to inser tif it is equal to
        else:
            self.value=value
                
    #we will checkif the key matches the key inside
    #because this is somehow like a bst we  check if the kjey matches the key inside
    def find(self,key):
        #we will use the normal find because  after nserting the tree is balaced
        #we will check if the self is a none so as to return a none while serching
        #this willensure if there is nothing in the key it will return a none
        #compared to insert which creates a nodeif the self is anone
        #we will chck if the self is none independently because it indecates we have reached the termination point
        #the if keymeans we have found thekey that matches the self.keys
        #we themn  move tothe left and then right 
        #the left and right uses elif and the key==self.key dosnt use because they depend on the above two conditions
        #this was alsoseen during the binary search pivoting
        #thoug we used an elif because we were using the same value conditions
        if self is None:
            return None
        #we will then check for the left then check for the right
        if key==self.key:
        #we will return the vcalue of the key self
            return self.value
        #we willcheck  if the key is greater or lesser
        if key<self.key:
            #we will reccursively find to the left
            #we use the  self.left.find because python always fills for itself the self function
            return self.left.find(key)
        #we will reccuresively find to the right
        #because it is a block we use elif hence should satisfy any of the conditions
        elif key>self.key:
            #we use the self.right .find because python always fills the self function
            #we will reccursively find to the right
            return self.right.find(key)
        
    #we will then have to update
    #we will chck if the key macheches the key and then update the value
    def update(self,key,value):
        #we will update theself functions
        if key<self.key:
            #we will check if the self is a none and reccursivelycall tothe left inorder to maintain the tree structure
            if self.left is None:
                #we return the values of the treenode key,value
                #we give the self .left a tree likestructure to straigten it up
                #e wil giev the lefta value fuction to unpack it to  node
                self.left= Treenode(key,value)
            #we will else update the left after the recursive call 
            else:
                self.left.update(key,value)
        #we willcheck if it is greater and pdate the right
        elif key>self.key:
            if self.right is None:
                #we reccursively make the structure
                #we return the values of the treenode key and value back
                #returning the treenode key,value makes the structure of the ttreee maintainable
                #we will give the right a value function so as to unpack it
                self.right=Treenode(key,value)
            #we will then update the right structure
            else:
                #we update diectly because it is a self hence we cant even display the function in a correct manner
                self.right.update(key,value)
        #we will then update if it is not lesser or not gereater it means it probably is equal to
        else:
            self.value=value
    #we will then list every thing in inordertransversal
    #a none type error meaning there is a  none object being returned
    def list_all(self):
        #we should not return none during transversing because it is supposed to return a list of values hence will bring type error
        
        if self is None:
            return []
        results=[]
        #we wil list the same as a TREE NODE
        #we will fist have a list of resilts
        #a local variableis a variable that is accesible inside the function while a global variablecan be accesed outside a function
        
        #we check if the self.left has a left child or has no left child  if it is none eans it has nothing but if it is not none means there is a left and right child

        #we have to check for the none  so as to make the structure and dothe reccursive calls
        #data basedata structures use the none values to represent the lack  of something in a data structure
        #compared to the parse tuple where we caninsert a none here we cannot insert a none
        #the parse tuple list all doesnot check for the left is a none or right
        #if we do not dothe checking we will not have to do the reccursive calls hence the list all reccursive call will be terminated
        if self.left is not None:
        #we will then have to index the left additioned list and then append the keys we will call the left ressurively by using the list all
            results+=self.left.list_all()
        
        #we willthen have to append the results
        results.append(self.key)
        #we will then have to add the left indexes
        #we willcheck if it is not none because we are moving inside outwards
        if self.right is not None:
            results+=self.right.list_all()
        #we are supposed toreturn the results inorder to list all
        #returning the results ensures that the values from the left and right are added in one and then the final output is released
        
        return results
        
avltree=AVLTee(aakash.username,aakash)
avltree.insert(jaadhesh.username,jaadhesh)
avltree.insert(biraj.username,biraj)
avltree.insert(sidhat.username,sidhat)
avltree.insert(haemaeth.username,haemaeth)
avltree.insert(sonaksh.username,sonaksh)
avltree.insert(sidhat.username,sidhat)

print("avltree find",avltree.find("haemeth"))
print("avltreelist",avltree.list_all())

#lest build a default display function
#we will display from the ey moving downwards
#we will check fom the left right when the key i a none
#this prints the intersection of the trees
#we will then look at the left of the intersection and the right of the intersection if they are a none then we return the intersection one by one
#we will return each intersection of the root
#we willthen have to  do the function reccursvely to return to the bottom of the tree
#the display function is similar to the to_tuple function because the to_tuple function checks foe the leftand right is none
#this is because we are extractimng the data from the inside then we have to do it in a reccursive manner
#we then have to do it in a repetetive manner and use commas
#comapared to the transversals function where we have  to chenge from the  left and right but we are adding them to a list ofnumbers
#we will get the new usernamethen update with the whole value
#all the three use the same functionals because we are extractingbdata from the inside
#the insert function converts intoa return treenode(key,value) which is the same when creating a parse tuple  a function and then insert tothe left and right
#returning the treenode is a function that allows the structure tyo accomodate the none values
#the reccursive function inthe tree node is the returning of anode
#alse while finding we return none when there is a none
#while also inserting we check for the left and right and insert to theleft and right
#we check if the left and right is none before inorder to return it backto the original tree
#this ensures that the tree function is back to the same orderev if the left and right are none
#because it is an insert functionwe do not need reccursive callls
#for the fiuncd we need reccursive calls 
#we xhxk if the key is greter then we move to the left 
#we check if it is lesser then we move to the right
#we check if it is greater we move to reightelse move left
#if it is equal we return t the way it is
#comparing it to a real world situaton
#we have a tree we need to find some root we will keep comparing with the picture 
#ifit is not the same and is of the left category style we move to the left
#if it is of the right category we move to the right
#after vomparing if it is equal to the real node tree
#in the insert we will check from the tree if it is greater we move t the left if it is lesse left and greater move to the right
#we will thenreturn the whole node or the elf function to give the whole structure

#the insert function  nowinserts to the left and right inex 

avltree.update(haemaeth.username,haemaeth)
#We will then have check if the are bst
def isbst(node):
    pass


isbst(bsttree)

#all the three we use the self.insert instead ofusing the nodes if we need to use the nodes we can double pass the functions
#by using a dash
#the parse tuple does the opposite of the tree transversals it checks for 
#the parse tuple checksif the left and right is a none and then returns the key
#the trree ie the avl tree checks if the left and right is not a none
#the parse tupe works outside in where we have to chec ifthere area none
#the insertworks inside out so when there is a none ot termionates



