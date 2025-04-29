#we will have a  binarysearch that will look for the card matching the query
#we will also have a count rotations  that will count the number of rotations that cards have been rotated
#we will also have a function that calls out the rotatted list and searches if the cards matches the query
#we will come up with example inpts and outputs
#we willcome out with our solutin and state themin plain english
#we cant run directly on rust because python and rust are independent
test={"input":{"cards":[1,2,3,4,4,5,5,5,6],"query":5},"output":6}
#we will have l and hi value function so that we can continue dividing the functions into halves
#we will have a while loop that checks for the lo to be less than or equal to the hi so that we make sure there are cards inside
#using the lo<=hi is more efficient because when doing a binary search we want to include the end points and see if they compare hence the end pointdtd cover for the equal sighn
#we will also chck for the cards that amtches the query by dividing the query by  half eachtime
def binary_search(cards,query):
    #we will have a while loop to checkfor the lo and hi but we have to check for the = because we want to move to the end
    #we willhave a while loop that will checkfor the lo<=hi
    lo=0
    hi=len(cards)-1
    while lo<=hi:
        #hee we will have the mid calcuated
        mid=(lo+hi)//2
        #we will also have the mid_card function
        mid_card=cards[mid]
        #we will now compae the cards at the mid to the quey and aso the cards before the mid
        #we willl first check if there is a md function before
        #we will first directly check for the midcard and then check now if there are two midsso that we dont check an empty cards list
        if  mid_card==query:
            #but before returning the mid we will check for the value of the function before
            #we mainly check the mid to be greater tham zero to avoid error when accesing the mid function of the card before the mid
            if mid>0 and cards[mid-1]==query:
                #we will return the lft soas to return the first card at the index
                hi=mid-1
            #we will return the mid
            return mid
        #we will then move to the left and right resprvctively but use independent if stetments so as not to tamper withthe meain atatement
        if mid_card>query:
            hi=mid-1
        else:
            lo=mid+1
    #wenwill then return a negative 1 when we find nothing
    return -1
        #we then check for the left and the right so that we continue searching fr the loop
print(binary_search(**test["input"])==test["output"])
#we will have a function that counts the number of rotations
#we will have a lo and hi function so that when we find the card at the mid index we can compre with the one before
#we will have a lo tobe qual or less than hi so that we can check for each card rotation
#the function willbe less than because we want to check for all the values and we want to return the lo
#if it was a less than ort equalto we would   not check every thing
#in count roattions we do not want to include the end points because the count rotations looks for a position on tye rotated list hence no equal sighn we will just return the lo
#we will have to return the position of the lo side sfter geting where the one is greater and before lies
def count_rotations(cards):
    #we will have a lo and hi and inside the whjile loop we will locate the mid card so that we can locate the cards posidion
    lo,hi=0,len(cards)-1
    #we will use aless than hi becaue we want to locate teh  cards at the lo position and dont want to check for the hi
    #this is because when the rotation is 0 we willreturn a zero hence we need to fncd the rotation from the bae of lo
    while lo<hi:
        #we will  calculate the mid card in the while loop because the mid card is alays calculated in the while loop
        mid=(lo+hi)//2
        #we will check for the cards befor the mid card and also check if there is a card before the midcard
        mid_card=cards[mid]
        #we will then have to check  for the cards befor amd the index of the  mid so that we mae sure that there is a value before
        if mid>0 and mid_card<cards[mid-1]:
            #we will then have to check for 
            #we will then return  the mid
            print(mid)
            return mid
        #we will either move left or right to make sure evrything is searchd
        if mid>0 and mid_card>cards[mid-1]:
            lo=mid+1
        else:
            hi=mid-1
    #we will then return a zetro at the end

    return 0
test={"input":{"cards":[5,6,7,4]},"output":3}        
print(count_rotations(**test["input"])==test["output"])
#we will also have a function that wiull be used to count the rotations and return the query hence aply both the above
#we will have a lo and hi so that we can locate the mid and compare with the card befor and also check which side we are gong to
# search for sorting
#wewill have theless than or equal to function because function because we want  to compare the cards withthe  qeury
#in a locate card function we will use the mid card and the query as the pivots
#but first we will check for which side we are in by comparing the mid and the lo hence a lees than or equal to because we want toinclude the lo card``
#we will then have to check again which side the quer is and then return the card by cmparing thisare all done in a whileloop because of searching
def locate_card(cards,query):
    #we will have a lo and hi because we watntto compare the pivots and the wuery
    #mark yo  this doues not have a midcard
    lo,hi=0,len(cards)-1
    #we will have  a while  loop that will be used to locate the middle card will use the less than or equal to because we are comparing
    #itas only that the mid function is being diverted
    while lo<=hi:
        #we will have a mid which will be lo+hi //2 so that we can modify the mid_card
        mid=(lo+hi)//2
        ##we will first have the midcards for comparision
        mid_card=cards[mid]
        #we will now check which side is sorted
 # test={"input":{"cards":[5,6,7,1,2,3,4],"query":1},"output":1}       
        #checking for the cards at the lo index and if it is greater than the mid it means the right is sorted
        if mid_card==query:
            print(mid)
            return mid
        if cards[lo]>mid_card:
            #the above function means that the right is sorted
            #we will first move to the right
            if cards[lo]>mid_card>query:
                #kama ya chini ni mingi kuliko ya kati kati na ya katikati ni mingi kuliko tyenye tunatafuta tunarudi left
                #tunamove left kama io mid ni mingi kuliko query kumaanisha iko left
                hi=mid-1
            #tunamove right lo ni mungi kuliko ya kati kati 
            #we will check otherwise where  the midcard is lesser than the query
            lo=mid+1
        #we will then check the other side of sorting
        #thisis when the crd at the loindexx is lesser than the mid
        #e will move the cards to the  right
        else:
            lo=mid+1
    #we will then return a negative one ,meaning not found
    return lo
                
            #na kama ni ivyo vingene
        #we will then check for the  s

test={"input":{"cards":[5,6,7,1,2,3,4],"query":1},"output":1}  
print(locate_card(**test["input"])==test["output"])     
        