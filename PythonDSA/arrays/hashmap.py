#we will have a hashmap where we reffer them ass puting balls in a field and and we can see everthing key value
#time complexity is o(1) and space complexity o(n)
MAX_SIZE=4096

#we will have teo kinds of hashmap
#this  can storean unlimited number of things unlike the other this can store even 5 keys
#the problem is that collisions might leed to overwriting and increase the leght

class Hashmap:
    #wewill store in the bucket but use the _ this is known as a chained  hence ther are connected to each other
    #we put themax_size to be equall to MAX_SIZE to allow for flexibility
    def __init__(self,max_size=MAX_SIZE):
        self.data_list=[[]for _ in range(max_size)]
    #we will also have a hash function
    #because it is an inbuilt function we will have a dash at the begining
    def _hash(self,key):
        #we will return the hashed index 
        #we will get the index  
        #the len of self.datalist means the whole function represented
        #not only the ones that contains values
        #this means it calculates the index according to the whole function
        return hash(key)%len(self.data_list)
    
#this only stores key,value pairs inshort single keyvalue pairs
#the key value pairs must also find them  selves
#each key value pair is stored at its own 
#we will ghave to get a valid index
    def _get_valid_index(self,key):
         #we will have an initioal index that we will  use to modify
         #the self.hashkey returns the index 
         idx=self._hash(key)
         #we will have a while true that is always used to modify a value
         while True:
             #we will get the  kv atbwhich the current index would be that contains the eyvalue pairs
             #we give the kv to every self.data list at index idx
             #thisis a lso seen when assigning the bucket some values
             #where the bucket represents everythin in the inside and can be modified
             #this was also seen in the user data base where we gave the for i in self.users
             #thei represents a single function in the whole thing
             kv=self.data_list[idx]
             #we will distinguish the key value from then kv
             #we will check if the kv is none inorder to return a  index that we will use to store the values
             #we will check ifnot bucket to properly detect empty bucket in the leist
             #iff we use if kv is none we will have to explicitky checkeverything in the bucket if it as a nonevalue
             if not kv:
                 return idx
             k,v=kv
             #we will compare if the k==key
             if k==key:
                 return idx
             idx+=1
             #we will check if we reached the last index
             if idx==len(self.data_list):
                 idx=0
                 
             #we will make the idx to be a zero
             #the not ennough values error occurs because there are no values in the given index
             
    def insert(self,key,value):
         #we will have to insert to where there is no one
         #we have to insert t the none
         idx=self._get_valid_index(key)
         #because  this is where more than three people might share
         #we will have a bucket where they will pay once
         #the bucket stores everything insde which is in he idex
         #the bucket represents the _ and hecnce it can storre as many values as it wants
         #this is like getting for users in self.users in a self.users functtion which contains an array
         #we will then have  to modify the bucket by enumerating
         bucket=self.data_list[idx]
         #we will then have to insert the key value
         #but because it is chained meaning manypeaople might live at one place
         #we will look for each individual in the two when enuerating the houd and isert i at the individual house
         #for the individuas who are living intwo weinsert two
         #the enumerate is used to put three values hence track the index and the value
         #an enumerate is a function that is used to loop over a string or listwhile keeping track of the index
         #hence we are enumerating overt the bucket while keeping track of the index 
         for i,(k,v) in enumerate(bucket):
             #the house of each individual can be insertedby the key value
             #we will check if the one person wants to relace then we replace
             if k==key:
                bucket[i]=key,value
             #we will then retur the answ 
             #we return so as to make sure there is no collision during searching again
             #we return after enumerate to unkeep the track of the index
             return 
         # we will nowadd infron t of the list by apending
         #we add tothe bucket which contains the idx hence the bucket represents the whole value of the function
         #we ad to the bucket which conatins the key vaues
         bucket.append((key,value))#this appends each bucket
         #appending a bucket means that after geting the index we add tothedata list where we want 
         #the data list has an index of _ and the bucket has no limitations it can add anytthing
         #the _ represents the index for each individual
    def update(self,key,value):
         #we will return the insert function as they are similar
         #when we returning meann we are duplicating the code  function rather than just reusing the code
         self.insert(key,value)
    def find(self,key):
         #this will be used to look for the people after they paid individually
         #will have to enumerate through each room and check if the key matches the value
         #lets get the index first
         idx=self._hash(key)
         #we wil get the data index of the key passed which is equalto geting the room
         #the bucket represent where the data list is present
         bucket=self.data_list[idx]
         #we will then have to check for the for the individualls in the room
         #dowe need to keep track of the index whilefinding something???
         #the answer is a no as we only need to return a value
         #this is because we do not need to modifythe structure
         #this is also why we donot chaange the bst structure in tree and bst hence it will destroy the structure
         #same here we do not need to  check for the indexwe just need to directly get what is inside
         #we will have kv to be in the buckets which means the individuals and then divid the kv by 2
         for kv in bucket:
             #we will then divide it into two this was also seeen  during the geting index where we divided the kv again to get the valid index
             k,v=kv#we compare if the key inside the bucket is equalto the real key then we return th value
             if k==key:
                 
                 return v
             # everything in the self.data list
         #because the balls were listed individually  
         #we will have a retun  all thet is a return the self .data list because it is stored oin the inside of a computer with a o(n)
         #alogarithms complexity
         #compared to the tree node where we have to append individually becaus eof o(1)space compexity where the complexity 
         #the o(1) space complexity means that it is stored in the outside hence there is no data inside the computer
         #in the real world the balls atre just given the way they are there is no need of touching them","244555")
    def list_all(self):
        #the bucket is a representation of everything
        #the kv is what is inside the bucket hence we will return what is inside
        #we must have a [] because it  returns alist of items
        #the brackets returns one at a time and is efficient for tuples which we need toreturn one at a time
        #the [] has a memory of list while a bracket has a memory of one at a time
        #while listing all in treenode  we use a list all that returns a single
        #we will have a list beacause we want to retuyrn a list of every thing at once
        #the bracket is ude for reversing in the to tuple hence the use of coma and not the plus sign compared to the listall
         return [kv for bucket in self.data_list for kv in bucket if kv]
hashmap=Hashmap()
hashmap.insert("mike","listen")
hashmap.insert("perister","ster")

print(hashmap.find("steve"))
hashmap.update("steve","mavi")
print("updated steve chaining",hashmap.find("steve"))
print(hashmap.list_all()) 
class Hashmap:
    #we will store each and every in their individuals hence this is a none cheined and there is noconnection with each other
    def __init__(self,max_size=MAX_SIZE):
        #unlike chaining this  reccords each individualls in their own
        #but this only ca reccrd akey,valye pare or a limited pairr compared to the other
        self.data_list=[None]*4096
    def _hash(self,key):
        #we will return the value from the hashing function the value that isof a given indez
        #this will map a kek value to the given size and will retive to the o(1) function
        #the hash does ths by simple athematical calculatios
        return hash(key)%len(self.data_list)
    def get_valid_index(self,key):
        #we will have an idx that we will use to modify
        idx=self._hash(key)#this gets the index that is being hashed
        #we will then have a while loop tah will be used to modify thehash functin
        while True:
            #we will then  have to give the general values at the idx a function value
            #aftergeting the data listband the idx which we did not know we then put a value that will be used to modify the 
            #we will then   use then index that we got to dipute intotwo and then modifyeach ofnthe two
            kv=self.data_list[idx]
            #we will split the kvinto two
            if kv is None:
                return idx
            k,v=kv
            #we will check if the k==key
            if k==key:
                return idx
            idx+=1
            if idx==len(self.data_list):
                idx=0
    def insert(self,key,value):
        #we will have an initial index and we willl install at the [] which willfind the index directly
        #unlike- where it contains a single list ths contains different lists
        idx=self.get_valid_index(key)
        self.data_list[idx]=key,value
        #we insert directly in the index thats why westar with the self.data list at theat index then we insert
    def find(self,key):
        #we get the index of the  key that is being searched 
        idx=self.get_valid_index(key)
        #we will give the kv to the data listr at the index of the incomingh key
        kv=self.data_list[idx]#we got the index of the data thatis being passed
        #mark you the data are stored in index 
        #while findingwe locate the index by callculating the data number function of trhe data list
        #we then have to sepparate thekv intyo two and see if it matches the key
        #this is after geting the data being passed  bycalculating the idex we separate and check if the k==key we then retunr the valuewe check forthe  
        #we separate the two so as to return the v
        k,v=kv
        if k==key:
            return v
        #we will ahve to check for the individual balls listed individually the find the ball that we want individually
        #the ball we will not alter the positions but checkfor the balls individually
        #we will then  have tocheck for the balls matching the key by giving everything in the bucket a value function
        #we will have an indexof the value and now compare the index data to the key and return the value
        #this is looking for  balls as we are already now the index the function will only call for the ball and compare with the key andreturn the value
        #becausethey are arrranged oindividually we can reach a ball faster hence we will just mneed to check which index
        #we don not keep track of the index while finding in a hashmap because hashmaps are good for fast key look ups hence keeping track is bad
    def update(self,key,value):
        #we will reuse the code
        self.insert(key,value)
    def list_all(self):
        #in list all we list everything in the insidewhen we return the sef.data list alone we will return everthing in the selfdata list including the lists
        # we do not have a bucket so we will return obnly the kv pairs in the self.datalist
        return [kv for kv in self.data_list if kv]
    
hashmap=Hashmap()
hashmap.insert("steve","888888")
hashmap.insert("wayne","244555")
hashmap.insert("mike","2345533")
hashmap.insert("perister","998474")

print(hashmap.find("steve"))
hashmap.update("steve","mavi")
print("updated steve",hashmap.find("steve"))
print(hashmap.list_all())
#what happens is that weget a hash value and modify the hash value so that we will use it latter
#the hash value is modified by using the idx and checking foe all the values of the hash
#we use kv =self.datalist[idx] it is also similar with for i exept it diggs deeper by geting thek,v in the kv
#we will get the distinct values and then check for them after geting the distinct values
#and then modify whet we wanted using the distinct values
#so if we are lookingb foe a value we give equals and look for a specific value and eturn the answer
#because its a whiletrue it willcontinue seemlesly if it was a   a <= it will need a negative one at the end
#the  hashmap is like  moving at each door number and  giveing evry one a door number
#everry customer is given a door number is given a value function
#if you give some one the same door number then we have to move infront
#we have the option of sharing or the option evry one a door number
#every one number then there is low chence of collision hence one enters it will overwrite
#while many a door number they might add one and you willnot notice
#one adoor number is add to add 
#then during inserting many a door number is assigned a bucket which the will use to pay one
#but everry individual pays alone
#we will then  have to insert search and find
#a probing hash table handles collisions by looking for an empty slot while a chainingf hah table adds on top of the spot which might make even the key,vaue pairs to be even 4
#this leads to a waste in memory usage
#a probing hash table stores  by multiplying and does not use memeory hence you can chenge the storage
#probing hash tanble is similar to a treenode
#when looking for  a key value we look for something different
#chaining is similar t the self.users function where we are chained to one thing hence colision can occur
#lets reffer to chaining as puting the balls in a busket
#in a basket one canput more than one balls in it while individual probing on looksfor a individula index
#we check for the  values of the individual spaces 
#while we cant exchange
#in the bucket we can change add the values but we willhave to check for the place where we are adding inorder to acces it easily
#we will also have to check  by doing this we will have tocomare while carring the balls and comparing toindes
#in the probing we insertdirectly if it does not match we move toanother space
#during searching we give 
#GIVING A PICORIAL VIEW
#while inserting using an individual its like balls stored at individual places and you are tasked to access a ball directly
#we will insert to where there is nothing
#compared to the inserting in a house where there are many people where we can insert anywhere
#incase of collisions we insert the ball to another p[lace] here then insert pattern
#we can insert even 5people in one room and incase  of collisions we just insert in the same room
#wto finding we can find a ball direcly from the values
#we can also find the valuesdirecly because they are store in a bucket we will need to look for the index or the ddor number this is by enumerating and ooking for each dooe and then getting the specific door so that we can compare 
#we will the divide the people and compare then retiurn  the person match 
#we will have to look for the balls individually where we wiil look dirrectly divide then find the match and look for the balls soize value
#the update we will have to check for the ball if they match the value directky and return by adding to that palce this is called appending
#we will check  for the indix of each room then divide the rooms and no check if the people match the keyand return the information
#the list all in the probing hashtable we will have  to check for the individual balls and return the values in the list of then individual balls we will return everyball directly
#in the list all of the chaimed hashtable we will then have  to check for each of the rooms and  checking first they are called bucets
#we will check for each of the rooms in the bucket which is the plotti
#we will then have to return the kv in the bucjets of which the buckets are in the ploti and then we will have to return in  a list []
#the square brackets means kudaka kila kitu na kwanet
#the ()meanskudaka mojha moja na mkono



#WE WILL NOW HAVE A  FUNCTION THAT WILL DO AN INSERTATION SORT THEN A FUNCTION THAT DOES  A BUBBLE SORT
# problem is that we have a list of cards arranged in descending order or ascending order
#we re suposed to sawap cards in a mannerr likely to sugest that the one before is lesser than the one after
#what does inserting  mean 
#inserting ,means puting a card to a given index meaning we should have a given index at the start we should have an index
#we will then have to move one by one towards the end
#we willthen have a for loop that will check each of values in the index by listing them individualy
#the dash represents each element in the list
#we will  then get the index which is a i the i represents the index to be modifies
#we will then  have a jwhich is the number befor
#we will thyen have to check if the cards at the j index is greater than the j and then increase he i+1 if the number before is greater than the current
#so we will check if it is lesser we insert at the index aor mobve by one
#coming up withi example inputs and outputs
test={"input":{"cards":[3,8,1,2,4,5,6,7]},"output":[1,2,3,4,5,6,7,8]}
def insertation_sort(cards):
    pass
#the results shoul allow in cards and shuffle them
def insertation_sort(cards):
    #this makes the incoming cards not to be altered but return a single value
    sorted_cards=list(cards)
    #we will then have an initial index because we want to insert at the zero index
    i=0
    #we wiill then check for the  indexes in the cards
    #we do not use the raneg but we use the len becauuse we want to swap the index
    #we will the indexing in the lenghth extracts each index but we do not want to return the index we want justthe individual elements in the index
    #trhe range is used to acces indices for swaps
    #we use first the range and then put what range we want to aacces
    for _ in range(len(sorted_cards)):
        #we will then have to get the individual index so that we can  modify trhe indexes
        #we will then have to check for each  of the cards in rthe array
        #the i is used toacces each ellement 
        for i in range(len(sorted_cards)):
            #we will then give the j a value in each of the range in the sorted cards
            #the j-1 reprensents the last element of which is sorted 
            #this represents the last place of which the cards is sorted
            #this might be after sorting where the cards have been sorted are 
            #this is like walking and leaving a leg behind the behind keg is the j-1
            #we will then check forthe card before the one that we want to check
            j=i-1
            #we will then check for the value of the function before the index
            #we will check for the j and then check for the j+1 and leave the i
            #this tracks up to where we had reached
            #this is incorrect because it sorts cards compared on adjuscent elements you cant compare the legs of two different people the back legs
            #we will need to compare a key rather thancompare adjuscent things
            #we will chec for the adjuscent cards because the i is used to stad in between when swapping
            #when we are at a zero the i is used  to compare for the value inforont but as we continue moving to the front the i at onr it compares the adjuscenty values
            #we will check for then if j>=0 so as to prvent moving backwards because once we make a step there is no moviung back wards
            #checkingbthe j>=0 means that we are checking for the sorted valys hence not repeating oyurselves
            #we will start with the before
            if j>=0 and sorted_cards[j]<sorted_cards[j+1]:
                #we will break if the incoming is greater than the avaiable
                break
            #we will then add the i+=1
            #we willcontnue adding the  i
            #but then isertat the first index
            #while we continue moving the loop 
            i+=1
            #the i as it maintans the midle it move when one is inserted anfd then moes to the front to compare the two
            #the i acts as a magnet and repelant
        sorted_cards.insert(i,sorted_cards)
            
        #we will then return the sorted cards
    return sorted_cards
insertation_sort(test)
print(test["input"]==test["output"])
#we will now have a  bublesort alogarithm
def buble_sort(cards):
    #we will change the list of cards to be in the inside to avoid colisions
    sorted_cards=list(cards)
    #we  wil now have to get the values of the individual index 
    #this gets the individual indexes of the cards
    #the _ checks for the individual cards without cecking the index
    #we will now check for the individuals in the sorted cards
    #the _  is mostly used when we want to modify some value functions in the inside
    for _ in range(len(sorted_cards)):
        #we will now check the index that we will use to swap
        #this now checks for the individual cards in the i
        for i in range(len(sorted_cards)):
            #we will then have  to get an index before 
            #theindex willmostly be a j its the one that will be holding all the sorted values of the list
            #this means all the values that are before and  are of sorted manner in the list 
            j=i-1
            #we willthen popthe index at the j sothat we sort the numberes befor
            sorted_cards.pop(cards[1])
            #we will then exhance the cards and then continue moving tothe front with the i
            #we will first check for the function values that  are sorted to be greater or equal to zero when it is a negative then the code might break
            #we  cant allow the ones that are sorted to be lesser 
            #infact the ones sorted are waiting for the i to move infront
            #the i acts as a sorter while the j acts as the sorted cards in a order fasgion
            #we will then check for the values of the cards at the front indexes 
            if j>=0 and cards[j]<cards[j+1]:
                break
            i+=1
        #we will then return tyhe cards
        return sorted_cards
    
#we will then have a merge  sort
#a meerge sort we will have to divide at first
#after dividing we will then   have to sort the right and left hand individually
#we will then have to return the rihght and the left hand sort which will mark the total
#first we will have a function that divides the functions of the numbers
#we will  then have a function that sorts the numbers directly by interchanging them 
def divide(cards):
    #we will divide the cards into two theleft and then the right
    
    #we will then get the lo and hi so that we can get the midle of the cards and divbid the cards
    merged=[]
    #we will check if one side is empty we return a none on the side this is so as to aboid the merging of the []twice
    if merged is []:
        return None
    
    d_cards=list(cards)#listing items just return the items the way the were
    lo,hi=0,len(cards)-1
    #we will first  get the middle
    #most programs  will flor thge mid point bec ause wen got friom lo to mid and the mid is the floor
    mid=(lo+hi)//2
    #we will then get the cxards atr the left divided bby two
    #we will then get the left then the right
    #we will divide the cards in a rccursive manner
    
    left=divide(d_cards[mid:])
    right=divide(d_cards[:mid])
    #we will now have  to  merge the left and right
    #but what if the 
    merged+=left
    merged+=right
    #we nust start as  list of mnerges the functions this is also seen when isting all where we get the kleft and the right of the tree nods and then put them in a list all
    #we will then have to check what if we finish merging on one side and  the list becomes empty
    #we will then have to sort the cards ant the 
    #because the integer divides by two it willroud of to the next
    #we we will get the right and the left
    #we will then return the merge
    return merged
#we will then have to sort the right and the left in a systematic way
#wewill now have to change the left and the right irectly
#but we have two functiuons
#we will have to change the cards into list
#wewill then have to look for  the is in tghe cards to intercahnge we will have a j
#we will then cahe the i and the jafter poping
def sort_merge(cards):
    #we will change the cards into list
    #this is so as to maintain the incoming structure to avoid collisions
    sorted_cards=list(cards)
    #we will then have  ty checkfor the _ so as to modify the indexes
    #the _ is like geting the exact location that we will use to shuffle people in the dome
    #its like kauachiliathe thing that are locked so that we can reshufle them
   #this is like announcing for shuffle in a dorm
    #mark you we maust have the len of cards beacaause it is the interger andthe intergers are the ones that are supposed to be modified
    for _ in range(len(cards)):
        #we will then get theindividual intergers
        #the i now means the individuals in the dorm
        for i in range(len(cards)):
            #we willthen get the indexes befor the number
            #of which is like the back wards foot hich will be used for modification
            #this shows the leg that will be used to hack
            #this is like the sorted parts where i reresents the chuchu when we move it might stay behind or move to the front
            j=i-1
            #we will then get the i and the j so that we can reshuffle andd walk
            #we will even check if the  legs befor and after when to insert when one os longer or shorter
            #when one isshorter we staybehind but when shorter we increament the chuchu by one so that we can continue sorting t the front
            #we will then check if the j>=0this is as to check whether the j is not moving back wad but is moving forard
            if j>=0 and cards[j]<cards[j+1]:
                i+=1
                #we will then interchange
                cards[j],cards[j+1]=cards[j+1],cards[j]
        #we will then return the cardsdirectly
    return cards