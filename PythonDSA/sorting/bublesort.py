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
    #we will have a lo and hi given the vaues
    lo,hi=0,len(cards)-1
    #we will check for when the lo is less than hi so that we return the lo but because we want to return the mid we will check for less than or equal to
    while lo<=hi:
        #we will divide the mid by two
        mid=(lo+hi)//2
        #we willget the card at the midle index
        #so that we can use toget for the card before
        mid_card=cards[mid]
        #if the card befor is greater then we return the mid index
        #we check for the mid tobe greater than zero   so that we make sure that it doesnot return an index error while accesing the card nefor
        #this is good for comparing the rotations and returning the value
        if mid>0 and mid_card<cards[mid-1]:
            return mid
        
        if mid>0 and mid_card>cards[mid-1]:
            lo=mid+1
        else:
            hi=mid-1
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
    #we will check for the lo and high and gibe them values
    lo,hi=0,len(cards)-1
    #we will have a while loop that will exhaust till the end
    #it exhause till the en because we want to loo for the card at the lo posiion
    while lo<hi:
        #we will get the midle index while in the while loop
        mid=(lo+hi)//2
        #we willlhave a mid_card function which will present card at the mid index
        mid_card=cards[mid]
        #we  will check for the sorted part
        #we will first check idf the midcard is equal to the query
        if mid_card==query:
            print(mid_card)
            return mid
        if cards[lo]>mid_card:# means that the right hand is sorted
            #this is used to compare the mid and the query
            if cards[lo]>mid_card>query:#this means  that we are in the right hand and the mid is greater than the query
                lo=mid#if we are in the right and the mid>query we will try to move to the right then left
            #we will check for the hi which will be the mid but the lo will  be mid +1
            #this is because we want to return   
            hi=mid-1
        #we will then check for the if the lo islesser than the mid
        #this means the left is sorted
        #we strt from the left comparing the query will in the left if it is lesser we move left
        #ese right 
        elif cards[lo]<mid_card:
            if cards[lo]<mid_card<query:
                hi=mid-1
            lo=mid
    return lo
test={"input":{"cards":[5,6,7,1,2,3,4],"query":6},"output":1}  
print(locate_card(**test["input"])==test["output"])     
        