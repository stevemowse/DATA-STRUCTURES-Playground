#QUESTION 
#I am supposed to look for a given card arranged in an decending order givenm the query

#state the problem clearly of which i have stated above
#Come up with example inputs and outputs
#come up with a solution irregadeless with the space and time complexity
#come up with test cases to overcome incoviniencies
#come up with a correct solution
#analyse the alogarithms complexity
#then test


#COMING UP WITH EXAMPLE INPUTS AND OUTPUTS
test={"input":{"cards":[9,8,7,6,5,4],"query":8},"output":1}
#we are supposed tocompare cards with the query so ewill allow two of them in
#we are also supposed to come up with a single output which is the position of the card that matches the query
def locate_cards(cards,query):
    pass

#COMING UP WITH THE CORRECT SOLUTION
#THE LINEAR SEARCH EXPLANATION
#it is an o(n)both time and space complexity as it grows according to the input size
#compred to o(log n) which grows much slower to the complexity
#we will perform a linear search 
#we will have an initial position of zero
#we will move throughout the search one by one till we reach the end
#when we reach the end we willbreak out

def locate_cards(cards,query):
    #initial position
    position=0
    #we will have a while loop because we alreadygave the poition a name
    #this was also seen during my practice on geting a valid index of a hash table
    #the while true loop continues untill we break it
    while True:
        #we willcheckif the card==query
        if cards[position]==query:
            return position
        #otherwise we add the position by one
        position +=1
        #we then break when we reach the end point
        #compared to the lo<=hi
        #we have to break manualy rather than returnng the -1
        if len(cards)==position:
            break
#testing the solution
print(locate_cards(**test["input"])==test["output"])#the function at first stated a false this is beacause i had confued my testcase values
#but after modifying it brought back a true
#COMING UP WITH TEST CASES to overcome inefficiencies
#
#what if the list cards was empty 
#what if the list cards had repeated numbers  
#empty cards
test={"input":{"cards":[],"query":7},"output":-1}
###-------------#print(locate_cards(**test["input"])==test["output"])
#the function brout back an index out of range error meaning it entered the loop but did not find anything
test={"input":{"cards":[7,7,8,8,8],"query":7},"output":1}
print(locate_cards(**test["input"])==test["output"])
#the function brought a false because we were locating the second seven
test={"input":{"cards":[7,7,8,8,8],"query":7},"output":0}

print(locate_cards(**test["input"])==test["output"])
#it located a true now
#we will then come up with a solution to overcome the first ineficiency
#we will enter the loop if andd only if the ist contains numebers
def locate_cards(cards,query):
    #we will have a lo and hi
    #the lo will be the zero index and hi be the last index
    #we add the minus one to reduce inefficiency during the editing
    #we will also have an initial position
    position=0
    lo,hi=0,len(cards)-1
    while lo<=hi:
        if cards[position]==query:
            return position
        #else we increament the position by one
        position+=1
    #we return a -1 while exiting the while exiting the loop
    return -1
print(locate_cards(**test["input"])==test["output"])
#it returned a true
#WE NOW HAVE TO ANALYSE THE ALOGARITHMS COMPLEXITY
#the above is of o tothe en hence time and input size increase with each input
#to overcome this we will undergo an o(logn) alogarithm
#we will come up witha search that pics upthe midle

#we will have abinary searchthat will locate the mid point
#we will then have to give the results avalue function
#we will then have to return ass steted
#at the end we have to return a -1
#In a binary search we do not assign the mid beacause the mid is temporary and we do not need to assign while looking for the temporary mid
def binary_search(lo,hi,condition):
    #we will have a while loop
    #the while loop is done about the mid and cndition
    while lo<=hi:
        #geting the mid
        #the condition is themid
        mid=(lo+hi)//2
        #we will give the results name
        #the mid is passed into the function from here
        results=condition(mid)
        #we return back the mid
        if results=="found":
            return mid
        #we then move tothe left
        #we will use an elif statement because it is a block
        elif results=="left":
            hi=mid-1
        #we will then have to move to the right
        elif results=="right":
            lo=mid+1
        #we will then have to return a -1 when we reach thenend
    return -1
#we will now locate the cards
def locate_cards(cards,query):
    #we will use pythons writing a functioninside a function for flexibility
    #the mid condition is passed through  and modifiedin the while loop while it uses the lo and hi as their conditions
    def condition(mid):
        #we storeit inthe mid so as to compare with the numbers before
        #we will assign the mid_card to be the card at the mid index which is returnd because the mid card is a permanentvariable
        mid_card=cards[mid]
        #we will then have to check if the mid_card matches the query
        #we will first check if it is greater than or equal to zero meaning it is there
        #we will check if the mid card are many
        if mid_card==query:
            #we will first check for the number before 
            #we checkif there are two cards first
            if mid>0 and cards[mid-1]==query:
                #wereturn left to get the first value
                return "left"
            #return that the card was found
            return "found"
        #we will the use an if statement because the function is not a block
        #because it is in decreasing we will move to the left if it is lesser
        #we will check if the mid card is leser than the query we move to the left
        #we willuse an elif statement because it is a block
        elif  mid_card<query:
            return "left"
        #we will then have to move to the right if it is greaater than the query
        elif mid_card>query:
            return "right"
    #we have now to bring backthe binary searcg
    #condition is the only thing passed the rest are passed at the end inoreder to be inserted
    return binary_search(0,len(cards)-1,condition)
test={"input":{"cards":[9,8,7,6,5,4],"query":8},"output":1}
#the function returned a false so i have to think on how to modify it 
#the test case with reccursive number is the one that did not work hence i have to modify the alogarithm
print(locate_cards(**test['input'])==test["output"])
def locate_cards(cards,query):
    #the condition allows forthe mid which will be used to modify
    def condition(mid):
        #we will store the mid card so that we can look at the value before
        mid_card=cards[mid]
        #this is a function that will be used to check if the mid card is equal to query but if i
        if mid_card==query:
            #if it is equall we first check if there is a value before  then we check if it is equal to querrythen return left
            if mid_card>0 and cards[mid-1]==query:
                #we return leftso that we find the first element
                return "left"
            return "found"
        #we will then check forthe normall check
        #we will check if themidcard is lesser than the query then we move right
        elif mid_card<query:
            return "right"
        else:
            return "left"
    return binary_search(0,len(cards)-1,condition)
test={"input":{"cards":[7,7,8,8,8],"query":7},"output":0}
print(locate_cards(**test["input"])==test["output"])#it returned a true
#NB when looking for the first ellement we have to get the mid then after getting the mid we compare withthe value before


#WE WILL HAVE A FUNCTION THAT LOCATES THE  NUMBER OF ROTATIONS OF CARDS
#we have a sorted list of cards that are arranged in decreasing order but we rotated and we are asked to find the number of rotations
#we will check for the  the number of rotations

#we have to state the problem in plain english
#we have to come up with example input anf output
#we have to come up with a solution
#we have to comme up with test cases
#we have to come up with a new solution to cover the edge case
#we have to analyse the alogarithms complexity
#we have to come up with a new solution

test={"input":{"cards":[3,2,1,9,8,7,6,5,4]},"output":2}
def count_rotations(cards):
    pass
#COMING UP WITH A SOLUTION
#we will have to check for the mid card
#we will have a hiand lo
#we willcheck if the card before the mid id lesser than the mid if it is lesser we return the mid
#if it is greater we move to theleftwe have to check for the start and ending poition
#thiss will ensure that we rotate right fully
#we also have to checkfor the lat positions
#we will check if the card before the mid is lesser than the mid
#if the number before the mid mist be lesser than the mid so we go back
#if it is greater than the mid we move to the front
#we have two conditions if the one before is lesser
#to move to the left and right we ill lok at the lower
#if the first card is lesser than the mid we move to the left
#if the first elsewe move to the right


#if the one before is more
#if more we move to the left
#if lesser we we return the mid
#else we move to the right 

def count_rotations(cards):
    #we willalways have the two conditions first compared to the get index and the linear search
    lo,hi=0,len(cards)-1
    #we will have a while and mid
    #we will have a onlylow is less than high to ensure that there is no number before entering
    while lo<hi:
        #we will get the mid index
        
        mid=(lo+hi)//2
        #we will have to to store the mid card in order to utilise thenumber before
        mid_card=cards[mid]
        #we use the loand hi to debug the code correctly
        print("lo=:",lo,"mid=",mid,"midcard=",mid_card,"hi=:",hi)
        #we will checkif the midcard has a number befor and is not the first digit
        #we will check if the before is lesser so that we return the mid
        #wewill only return the mid if the number before is lesser than the mid
        #we will check if there is a mid before
        if mid>0 and mid_card<cards[lo]:
            #we will return the midback
            return mid
            
        #we will check if it is greater so that we return to the left
        #we will useelif because it is a block statement
        #we will check if there are twomids
        #w e will then retuern to the left and rightwe move to the left
        
        elif  mid>0 and mid_card<cards[lo]:
            
            hi=mid-1
        
        else:
            lo=mid+1
        #else if we are on the left we then check if the cards at 
    return -1
#we are looking for the smallest element
#we are looking for the largest element
test={"input":{"cards":[4,5,1,2,3]},"output":1}
print(count_rotations(**test["input"])==test["output"])#the function returned a false so  we have to modify it
#by applying the print duting the debuging 
#we look if the num print
print ("elizabeth mole")
#we have to look for a cretain position in a rotated list
#first we have to look for the rotations
#we will have to chexk for the greater card than the mid
#then we check if the greater card matches the  query if it matcheswe return  the mid
#if it is equal we move left w
#we will check if
#THE ABOVE FNCTION RETUNRD A FALSE SO  I HAVE TO RECHEACK MY CODE

#the cards will return a single output which will be the number of rotations

test={"input":{"cards":[4,5,1,2,3]},"output":1}
#we will have to check for thelowest number
#we will return the lowest number otherwise we move to the left
#and if left we movr tothe right
def count_rotations(cards):
    #we will have a function that stores the hi 
    lo,hi=0,len(cards)-1
    #wewill have a while loop that shows that there are cards inside
    #we make it to be only lesser because  we enter the cards if and only if there are two cards
    while lo<hi:
        #we will have to get a mid card
        mid=(lo+hi)//2
        mid_card=cards[mid]
        #we will have a midcard
        #we will then  have too check for the lowest number
        #we have to check if there are numbersbefore the mid
        #we then have to locate the card that is lesser than the number before 
        #if there is we return the mid we use the mid card so than e can return it
        if mid>0 and mid_card<cards[mid-1] and mid_card<cards[mid+1]:
            #we will return the mid
            return mid
        #else we will have to move to the left then right
        #we will use an elif because it is a block statement
        #we compare the mid and the  right most if it is greater then it must be on the right
        elif cards[mid]>cards[hi]:
            lo=mid+1
        #we then move to the right
        else:
            hi=mid-1
    return 0

test={"input":{"cards":[4,5,6,7,1,2,3]},"output":4}#the function returned a corrected code        

print(count_rotations(**test["input"])==test["output"])
test={"input":{"cards":[4,5,6,7,1,2,3],"query":2},"output":5}

#the def loacte cards will first look for the number of rotations in a crad
#it will look if the card matches the query then return the quer
#before checking ifit matches we willcheckif the vaue before is greater if greater we move to the left
#other wise we move tothe right
#and at long last return the querty
#if not we return a -1
#we will have a function that locates the cards in a linearsearch
#we will heve an initial position
#we make sure that the lo is lesser than the hi so as to enter and compare the two
#if not we return a zero
#we will have tocheck if the card at index position is lesser than the one at the position +1
#if lesser we return the position otherwise we increament the position by one

#the function is of a space complexity of log(n)#because we are comparing with the previous cards
#the function is of time  complexity of 0(n)#because search increases with the number of outputs
#the time complexity of on
def number_of_rotations(cards):
    lo,hi=0,len(cards)-1
    position=0
    #we will only use the less than because the less than presents
    #this is similar tothe mid>0  
    while lo<hi:
        mid=(lo+hi)//2
        #we will strore the mid_card to cards[mid]
        #the mid_card is used to store array of given functiontoone
        mid_card=cards[mid]
        #we will check if the cards before the mid is  greater than the mid
        if cards[mid-1]>mid_card:
            #if it is greater we return the position otherwise we increament the position by one
            return position
        position+=1
    return -1

test={"input":{"cards":[4,5,6,7,1,2,3]},"output":4}#the function returned a corrected code        

print(count_rotations(**test["input"])==test["output"])#the function also returneda false
#we will check for binary linear search and differentiate
#the linear has lo<=hi because it is comparing with the outer card 
#we will have a position and keepincreamenting by one while comparing with the query

#on the will of rotations we aren comparing with the card before so the lo<hi becausee have to make sureethe cads are two

#we will then look at the  cards before  tahts why we have to make sure they are two
#we also have to look at the before cards and make sure they are lesser if greter we return mid
#else because  else we move to the left if the lower is lesseerthan the midthen right
#this is used tosearch for which side we look for first we will alwayssearch each half well inorder to maintain the efficiency
#we check each halfconcurrently because we need to maintain the alogarithms time complexity o(logn)
#by not maintaining the alogarithms time complexity we willl loose the purppose of the alogarithm because the time complexity will continue just to look for the purpose
#we check the card before because of the pivot is a the place where the mid card is stores
#where the midcard is stredis where the mid will return

#we also store in the binery search tocompare the number before ifthey are repeated
#comparing the numbers we will check if 
#the list converts tuples strings into a list
numbers=range(1,10)
print(list(numbers))
test={"input":{"cards":[9,8,7,6,6,6,6,6,6,6,6],"query":6},"output":3}
#we have to locate the first and the last numbers
#we will have a function that searches for the query but before it looks if the previous is also equal toquery if so moves to the left

#we will have a functio that checks if after is equal to query if so moves tothe right
#we will return the whole function
def locate_1cards(cards,query):
    def condition(mid):
        #we will have to give the mid_card a value soas to check the one before
        mid_card=cards[mid]
        #we will check if the mid is equal to query but before we check if the  mid-1 is equal to query hence return left
        if mid_card==query:
            if mid>0 and cards[mid-1]==query:
                return "left"
            return "found"
        
        #we now have to go to the left then right
        elif mid_card<query:
            return "left"
        else:
            return "right"
        
    return binary_search(0,len(cards)-1,condition)
test={"input":{"cards":[9,8,7,6,6,6,6,6,6,6,6],"query":6},"output":3}
print(locate_1cards(**test["input"])==test["output"])
#we will now check forthe llast card
test={"input":{"cards":[9,8,7,6,6,6,6,6,6,6,6],"query":6},"output":10}
#we will have a function that first checks for thequery
#this was seen same as looking for a rotation we first look for the rotation then move either left or right
def locate_lastcards(cards,query):
    def condition(mid):
        #we first have to store the mid_card into a place
        mid_card=cards[mid]
        #we have to check if the midcard==query and before checking we willl have to check  if the nid+1 isequal hence we move right
        if mid_card==query:
            #we have to checkif the mid are two
            if mid>0 and cards[mid+1]==query:
                return "right"
            return "found"
        #we have to return left then right
        elif mid_card>query:
            return "right"
        else:
            return "left"
    return binary_search(0,len(cards)-1,condition)
print(locate_1cards(**test["input"])==test["output"])
#we will havean initial position
#we will check ifthere are two andcheckif the one befor is greater or lesser otherwise we increament the position by one
#we return a zero if no rotations were made
def count_rotions(cards):
    #we will have an initial position
    #we could have a position infront 
    position=0
    #we will check if the position is lesser than the len of cards to ake sure we enter if there is a card
    #compared to the lo<=hi where we are lookin
    #this is more readable and does nt inquire subtracting one
    while position<len(cards):
        #we will have to check  if the position is greater than zero tomake sure it is in the second position
        #we use only the positionbecause we do not want the card to be stored into a variable we just want to return the card directly
        #if the last card is greater than the position we return the position
        #this makes sure the list cards continues moving increamenting by one
        if position>0 and cards[position-1]>cards[position]:
            #we return the position directly
            return position
        position+=1
    #we return a negative 1
    return -1
        
test={"input":{"cards":[4,1,2,3]},"output":1}#the function returned a corrected code        

print(count_rotions(**test["input"])==test["output"])#the functionreturneda true so themein issue  is how we enter the loop
#first we enter the loop if there are two functions inside hence position<len(cards)compared to the other where we enter the loop 
#we enter the loop when the lo<=hi meaning we have to compare only one when searching for a query
#we donot use the position =1 becaue we will be starting at the first position we need to start before and compare withe the one before 
#comparing the position tobe greater than zero make
#cards at index position-1 means the ast card cards[position-1]means cards[-1] which is the last card
#we know that cards[poition]means the first card and cards[position-1] means the last cards

#compared to the bimary search we compare the mid card to the 
#we will have a low to be less than hi
#this is becasue we need to enter the loop when there are two elements
#to avoid miscalculations and return a zero if there is nothing
#we have to check if the mid >0 to make sure thare are two numbers
#we then check if the last card at the before the mid mid[-1] because mid[1]and mid-1=0
#we will check if it is lesser we move ro the left
#if cards and the lo index is greater than high we move left otherwise right
#we will have a pivot function andleft and right function
def count_rotations(cards):
    #we will have a function that stores the hi 
    lo,hi=0,len(cards)-1
    #wewill have a while loop that shows that there are cards inside
    #we make it to be only lesser because  we enter the cards if and only if there are two cards
    while lo<hi:
        #we will have to get a mid card
        mid=(lo+hi)//2
        mid_card=cards[mid]
        #we will have a midcard
        #we will then  have too check for the lowest number
        #we have to check if there are numbersbefore the mid
        #we then have to locate the card that is lesser than the number before 
        #if there is we return the mid we use the mid card so than e can return it
        print("hi=",hi,"mid=",mid,"lo=",lo)
        if mid>0 and mid_card<cards[mid-1] and mid_card<cards[mid+1]:
            #we will return the mid
            return mid
        #else we will have to move to the left then right
        #we will use an elif because it is a block statement
        #we compare the mid and the  right most if it is greater then it must be on the right
        #we will now check if the mid is lesser than hi
        elif mid_card<cards[hi]:
            #we use the mid to avoid skipping the pivot
            #we return the hi to be equal to mid because it obviously lies in the left halfof the cards
            
            hi=mid
        #we set the lo to be mid +1 because it will obviously  located to the right hand side
        else:
            lo=mid+1
    return lo
test={"input":{"cards":[4,5,6,7,8,8,8,1,2,3]},"output":7}#the function returned a corrected code  
#compared to binary search of query which we look for the match,here we look for the pivot
#at first      

print(count_rotations(**test["input"])==test["output"])
#thenormal binary search we do not use the hi=mid because we already  compared the cards tothe query sowe need to skip
#compared to the other we do not need to skip 
def locate_1cards(cards,query):
    def condition(mid):
        #we will have to give the mid_card a value soas to check the one before
        mid_card=cards[mid]
        #we will check if the mid is equal to query but before we check if the  mid-1 is equal to query hence return left
        if mid_card==query:
            if mid>0 and cards[mid-1]==query:
                return "left"
            return "found"
        
        #we now have to go to the left then right
        elif mid_card<query:
            return "left"
        else:
            return "right"
        
    return binary_search(0,len(cards)-1,condition)
test={"input":{"cards":[9,8,7,6,6],"query":6},"output":3}
print(locate_1cards(**test["input"])==test["output"])
#we will now check forthe llast card
test={"input":{"cards":[9,8,7,6,6,6,6,6,6,6,6],"query":6},"output":10}
#we will have a function that first checks for thequery
#this was seen same as looking for a rotation we first look for the rotation then move either left or right
def locate_lastcards(cards,query):
    def condition(mid):
        #we first have to store the mid_card into a place
        mid_card=cards[mid]
        #we have to check if the midcard==query and before checking we willl have to check  if the nid+1 isequal hence we move right
        if mid_card==query:
            #we have to checkif the mid is greater than the lenght of cards meaning it is at the front
            #the len(cards-1) is a function that is used to check if there is a card before becaue there must be two inorder for the mid to be lesser than the len(cards
            # the minus 1 comes from the use of binary hence starts with a zero makinhg len of cards to be at the far most and mid be at the mid index meking it moving closer
            #so as the cards move closer we will move to the left then right
            if mid<len(cards)-1 and cards[mid+1]==query:
                return "right"
            return "found"
        #we have to return left then right
        elif mid_card<query:
            return "left"
        else:
            return "right"
    return binary_search(0,len(cards)-1,condition)
test={"input":{"cards":[9,8,7,6,6,6,6,6,6,6,6],"query":6},"output":10}
print(locate_lastcards(**test["input"])==test["output"])

