#   WE WILL HAVE A buble sort insertation sort and 
#we will also have a merge sort
#the differences come aninsertation sort is used to insert AFTER COMPRING THE CURRENT CARDS TOTHE BEFORE
#a buble sort is used to swap cards directly
#we will come up with example inputs and outputs
cards=[9,3,1,2,4,6,5]
output=[1,2,3,4,5,6,9]

#we will have to change the cards into a list of cards
#we will then look for the indxes and then the individeals
#we will compare the front and the ones before
#we will interchange the front and the ones before direcly hence tbhere is no need for j in the buble sort because we are not insertinf rather weare interchangeing

def buble_sort(cards):
    #we will change the cards into a list of cards
    #this is done mainly to avoid collisions
    cards_list=list(cards)
    #we will then have  to check for the i and the indexing because we want to swap the indexes and modify them
    #this is becaue we are accesing evry element and interswaping them this seems to be a smaller move but what do i know
    #we use the minus 1 because we do not want to reach the last element
    #we will get the individual indexs for modification
    #this is also seen in the hashmap which is not a probing hashtable where we can just  acces an element directly
    #the hah table usually takes the values of the individual index for modification
    #this gets the individula indexes amnt the i in the individual indexes
    for _ in range(len(cards_list)-1):
        #we will now get the individual values
        #this is like geting the individual indexesin the hah
        for i in range(len(cards_list)-1):
            #we will then  pass
            #because this is a buble sort we will compare the adjuscent values
            #we will have a while function sothat whenever the case happens we move and interchange the cards
            #this is also seen on the insertation because we want to insert a fnction while in the loop
            #a while statement is used for continues looping
            #the if statement in the merge sort is used because the functions have alsready been divided
            
            while cards_list[i]>cards_list[i+1]:
                #we will then  intechange the values at the index of i and the front of the indexes
                cards_list[i],cards_list[i+1]=cards_list[i+1],cards_list[i]
        #we will then haven to return thenfimnal cards list
    return cards_list            
#we will have to look for the individuals because we are only inserting
#we will have a current card that we will use to insert into the system
#we will then have to hava a j which is the card before
#we willthen  have an i that will be in the midle and will be used toiinsert
#when the position is found the i is insertted in the position of j+1

def insertation_sort(cards):
    #we willchenge the functions into an individual list
    #this is soas to avoid collisions
    cards_list=list(cards)
    #like the probing hash table we will just have individual functions at their own
    #this function inserts to theend comparedto the buble sort where we only swap
    #the inserttation sort wrks by building the sort in an increamental manner rather than a normalmanner
    #tghis is not the same in a buble sort because the buble sort does this by comparing adjuscent cards and this does not have to reach the end
    #thisis contrary to the inserttation sort where we add increamentally
    for i in range(1,len(cards_list)):
        #we will then pass
        #we will insert a given value at given indexes the given value 
        #we will have an initial value which i the curent cards and thenj and the j+1 while be the adjuscent value functions
        current_card=cards_list[i]
        #we will then have an addjuscent cards value function
        #we will then have a j function which will be the value of the cards befor it
        #this is likethe pivot where we check for the  values  of thenlowerandthe upper so that we can modify where to move
        #here the pivot is the j and the j+1
        #we will check if there is a functional number before or iside so that we can isert
        j=i-1
        #we will check if the card befor is greater so that we can move backwards byone
        #we willuyse a while state ment because we want the function to continueexecuting its self continously
        while j>=0 and current_card<cards_list[j]:
            #we will continue moving the j behind 
            #we will first put the j to be the current car
            #we will move the  j to the front
            #this function moves the j to the front whle leaving the i behind and if we find it after checking i
            #after checking i can repetative functions meaning that the values have repeated a coupleof times
            #we make the front to bethe behind by reducing it
            cards_list[j+1]=cards_list[j]
            print("cards j=",cards_list[j])
            print("cards j+1=",cards_list[j+1])
            print("_________________")
            #we continue moving behind
            j-=1
            #we will then have tomove bacwards by 1
            #we will then have toinsert at the j+1
            #this inserts infront after comparing with the j this is efficient to comparision and then inserting
            #we will then make the curecnt card to be the card at the index j+1
            #we will then find a place to insert
            #wewillthen have an if statement
            #after checking weather we move to the front 
            #after debugging second thoughts the cide has not touched the midle and the end
            #wethen make the front to be the main
            cards_list[j+1]=current_card
            print("curentcard=",current_card)
            print("cards j+1=",cards_list[j])
            #we willcontinue moving behind because after puting the current card tothe j we will make the j to be the j+1 and then 
    #we will then return the current card
    print("returnedcards",cards_list)
    print("currentcards that are outside",cards)
    return cards_list

#the merge sort will have a function that divides the cards like the binary search
#we will divide the functions first like the binary search tree 
#we will then have to check  for the left and then the right reccursively
#we will then return a merge function

def divide_conqure(cards):
    #we will check if the left is greater or lesser than the indexi
    if len(cards)<=1:
        #wewill return the cards if wehave one card
        #thishelps   to curb recursive dividions when there is nothing and alos clears the edje cases of a single card
        return cards
    #we will have to get the mid of the value
    #we will get the len of cards directly because we do not want to modifyt the mid
    #changing the cards into a list helps prevent modification incase we want to use the cards for later use
    #we have to check for the base case to ensure neeither is of a reccursive function shida
    #this is why there is a reccursion error during the  cards search because whenthe cards are exhausted itcontinues to search

    sorted_cards=list(cards)
    #we check the len of the sorted cards because this is what we want to be sorted
    #we dont use the -1 because we want to divide the partes into two equal parts
    mid=(len(sorted_cards))//2
    #we will then have to check for the cards 
    #we will then have to individually  look for the left and the right hand side of the cards like the binary search looking for when to put the midle function
    left=divide_conqure(sorted_cards[mid:])
    #we will then have to check fo the right
    #we use the sorted cards because they are the ones that are being modified
    #the merge sort divides the leftand the right withtimes then the dividion individuals are then put to the merge asort
    #this is used to divide the cards on the left and right to a base  case
    right=divide_conqure(sorted_cards[:mid])
    print("left",left)
    print("right",right)
    #we will then have to check for the merge 
    #the merge will paass the function bellow for the modification of the left and the ight funcvtion
    return merge_sort(left,right)
#this is a function that will merge the divided cards to one
#we will then have to check for the results which will store the functions
#we will then have an initial indx which is zeroon both ends
#we will then  have to check for the  left to be greater than the indes and right so tahtone of them should have not been exhausted
#we will then check for the left and rifht which is greater and append the left first and then append the right functions secondly
#wwill then  have to insert the rightsfunctions after inercanging everything
#we dothat by inserting to the results we then return the rsults
def merge_sort(left,right):
    #we will check for the len of cards so we can deffend maximum reccursion
    #this means there is no ro there is a single card in the list hence we return the cards directly
    if len(cards)<=1:
        return cards
    #after getion the functions of the merge
    #we willhave an initial lsit to store the merge fuynction
    #compared to otheres where we have a singlelist this list will be used to append the fynctionalvalyes
    results=[]
    #we will then have to check for the  left  to be available and also the rightto be available
    #we will have an initial index that we will use to modify to the next after passing a function either to the right or the left
    i,j=0,0
    #we will then confirm that there is something in thei and j compared toother functions where we search for the 
    #we will use an if loop
    #the ifloop is used to modify the leftand the right functions
    #this checks if there are functons in the left and right hence the left and right are notempty
    #we check ifthey are lesser to make sure there is avalue in the behind
    
    #the whileloop is used to increamentally extend to the left and the right
    #the while loop ensures that the function continues puting it to the results
    #we wuse the while loop to insert and return the right and the left shufling until one is exhauseted
    #compwred to the get index function
    #the while loop was used  to modify the i and j after geting the cards
    #we will move the j by one and also the i by one after inserting and makesure we have inserted everything
    #this is done by taking the elements at the given index and then adding them into the results rather than  than returning the cards
    #we use the indexto get the elements and add them tothe value function
    #this is like the binary search where we get the index and compare the index value and the real value
    #meaning in python we can alweays compare the value of the index and the real value
    #that is why we have to insert to the given indexed card merge instead of the whole because we are manupilating theindex
    #we will alwaysadd the function at the given index
    #here we willappend the individual function compared to the insertation sortwherewe move by  the middle
    while i<len(left) and j<len(right):
        #we will then check if the cards at the left are lesser than the cards at the right
        #we will check if the lefts values are greater than the right o that we can interchange them
        if left[i]<right[j]:
            #we will then appentd the left values and then move the j by one
            #we will the move by one to ensure that we finish allthe left and the right
            results.append(left[i])
            i+=1
            #we will then insert the right value functions
        else:
            results.append(right[j])
            #we will then move the j+1
            j+=1
    #we will then return the results
    #extend is a function used toaddelements of a tuple to an existing list
    #zenye zilibaki zinarudishwa ndani
    #we must start from the front to the end
    results.extend(left[j:])
    results.extend(right[i:])
    #we will then return the finall results
    return results
print(divide_conqure(cards)==output)
print(buble_sort(cards)==output)
print(insertation_sort(cards)==output)