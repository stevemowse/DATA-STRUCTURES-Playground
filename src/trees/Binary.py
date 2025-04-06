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