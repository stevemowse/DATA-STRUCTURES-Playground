#we will state the problem in plain english
#we want to sort the following list in a decreasing order
cards=[1,2,5,3,4,7,6]
output=[1,2,3,4,5,6,7] 
#we will come up with a nrmal solution
#we will check for the cards if the list is empty to provide a dividion that is not reccusive and esscape the empty card test case
#this is so ass to prevent reccursion error which is when dividing a card to the minimum of the card 
#we will check for the left of the cards reccurily and the right then pass themto the merge sort 
#the depth function is used to help in debugging hence contacted to the base case of the value function  
def merge(cards,depth=0):
    #we weill have to check for the none of the reccursive calls
    #we will check if the len of card is lesser than one we return the cards lesser or equal
    #we will not use the none function beccause that limits it to a base case what if one card is passed
    #we will print for the merged function of the eft and right value function combined to one the left and right value function
    #we will merge from the left and right into one 
    #this function shows which part of the left and ight are beimng combined during the proces
    print(f"mergedepth= {depth} :{cards}")
    if len(cards)<=1:
        #we willl return the initial cards if the len of cards is lesser than or equal to one
        return cards
    #we will have to check for the hi and the lo so that we can  get the mid and divide the functi
    #we will have toget the mid
    #we use the lo and hi for binary search but the mid=len(cards)//2 isused besst mainly for safe slicing rather than the whole
    mid=len(cards)//2
    #we will print the depth as we continue moving inwards
    #what happens as we move to the left of the merge
    #we will divide the left reccursively
    left=merge(cards[mid:],depth+1)#as we move to the indside we contunie adding the depth in the inside which will be a single value
    #wewill then check for the right up to the base case
    right=merge(cards[:mid],depth+1)
    #we will then retrurn the right and left to the function tothe base case
    #when it is lesse than 1 we eturn the card meaning it is the base case toprevent more reccursion
    #we wil then resurn the base cases of the left and right tothe merge sort
    #we will then pass the depth to the merge sort alogarthm for it to divide
    return merge_sort(left,right,depth)
    
#we need to get a dividion of the merging at depth of both side both the left and the right
#at first we are dividing the values at at secont we are combining the values of the function
#hence merging at depth and merging function when utilising the merge at depth function
#we willrecieve the merge sort functions and then get the initial value of the merge sort we will then print the depth of the functions
#we will then check for the values by giving index we willalso have a results and then appen to the results and then at the end add the left funtions and the right to the results\
def merge_sort(left,right,depth=0):
    #we want to print the depth of the merge sot=rt and the merge
    #printing outside does not increament the depth while mob=ving the chain
    print(f"merged {depth}: {left},{right}")
    results=[]
    i=0
    j=0  
    #there is a difference betweeen merged depth and merged
    #merged meansthe number of combined while merge depth means the depth in the inside
    #we will havce to print the merging at depth left and rightinto one because we are reccursively mergingthem
    #this function shows when the left and right function are being merged
    #printimg inside the while loop will show eachmerged opperation bringimg about more noise while printing outside the loop will show after the merge has occures
    #in the whiule loop it will show each comparision

    while j<len(right) and i<len(left):
        #we will have to check for the left index of i and the right index ofi
        if left[i]<right[j]:
            #we will then add the left index functions of i
            results.append(left[i])
            #we will continue adding the i by one while aapending them to the values
            i+=1
        else: 
            #when the left is greater then wee add the right because it was already divided there is no need to modify the valiues
            results.append(right[j])
            #we will then keep increamenting the j by one
            j+=1
        #we will keep increamenting the aliteration at each depth
        #we will then print the merged 
        #we willthen extend the values of the left
    #we use the results .extend in the whgile loop means it calls everytime we call the extension
    #we do not extend in the while loop because extension makes the while loop to be extend after each ateration comparision instead of comparing all and then extending the residual functions
    #this kmayt return an inballances functional lists
    results.extend(left[i:])
        #we will then extend the values of the right
        #extending means we dont include the parrenbthessis we just extend everything on the right and then etend everything on the left
    results.extend(right[j:])
        
    print(results)
        #we will then return the results final values
    return results
print(merge(cards)==output)
#maximum reccursion depth error meaning it reccusivelty called itelself and python breaks it so that we do  not get a code breakage
#here we wil get the len(cards)//2 to prevent the slicing and also use the cards <=1 we return the cards to prevent further slicing of the cards
#index error mean theinde is out of bound or we have tried to acces the index and we cannot find the index
        