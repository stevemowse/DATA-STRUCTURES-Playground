import csv#used to import the built in csv reader that is used to read documents
#this isa function that will store the values at the given data indexes

class NetflixTitle:
    """Class to represent a single Netflix title with all its attributes"""
    def __init__(self, data):
        self.show_id = data['show_id']
        self.type = data['type']
        self.title = data['title']
        self.director = data['director']
        self.cast = data['cast']
        self.country = data['country']
        self.date_added = data['date_added']
        self.release_year = int(data['release_year']) if data['release_year'] else 0
        self.rating = data['rating']
        self.duration = data['duration']
        self.listed_in = data['listed_in']
        self.description = data['description']
    #the str function is used as a representatable
    
    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.type}"
#a binary search tree is a tree that balances itsef hence the left is lesser thanthe node and right and vise versa
class BSTNode:
    """Binary Search Tree Node"""
    def __init__(self, title_obj, key_field='title'):
        #this will be used to get the keyfield given the title object
        #the get attribute is a self built in used to get the value when the tittle object is stored
        #this isused to get the tittle directle just lik the getitem
        self.key = getattr(title_obj, key_field).lower()#the lower is used to universialisal to covert all the string uppercase to a lowercase
        self.title_obj = title_obj
        self.left = None
        self.right = None
#the supper init mmethood ensures thatthere is inheritance of the methods

class AVLNode(BSTNode):
    """AVL Tree Node (extends BSTNode)"""
    def __init__(self, title_obj, key_field='title'):
        super().__init__(title_obj, key_field)
        self.height = 1

class NetflixSearchSystem:
    #this isa function that will allow in by the file name
    #the function also allows the data to be stored in
    def __init__(self, filename):
        #the self.data will have a list brackets
        self.data = []
        #this will be used to be sorted by title 
        self.title_tree = None  # BST sorted by title
        #this will be used to be sorted by theyear
        self.year_tree = None  # AVL tree sorted by release year
        #this is used to return the data by loading
        self._load_data(filename)
    #the first dash means a built in function used only within the code parameterd 
    #the load data is used onlyto open the data files
    def _load_data(self, filename):
        """Load data from CSV and build search structures"""
        #this is used to open the data with a new line and the utf is used to remove the language barrier
        with open(filename, newline='', encoding='utf-8') as f:
            #this is used as a reader file which will read the file name
            #the dictionary reader will read everything
            reader = csv.DictReader(f)
            #the row will return each line of row
            for row in reader:
                #this makes the whole title to be on the netflix row
                title = NetflixTitle(row)
                #this will be used to append the tittle and the year tree remaining
                self.data.append(title)
                #this is used to insert the title and the year differently at once
                #because titles tree are randomly distributed we insert in a bst
                self.title_tree = self._insert_bst(self.title_tree, title, 'title')
                #because years need to be balanced we insert into an avltree
                self.year_tree = self._insert_avl(self.year_tree, title, 'release_year')
    
    # Basic BST operations
    def _insert_bst(self, root, title_obj, key_field):
        """Insert a title into BST"""
        if not root:
            return BSTNode(title_obj, key_field)
        #this is used to get the title and automatically get the field
        key = getattr(title_obj, key_field)
        #if the key is a string then it is converted into a lower case
        if isinstance(key, str):
            key = key.lower()
        #if it is lesser than the root.key we insert tothe left
        if key < root.key:
            root.left = self._insert_bst(root.left, title_obj, key_field)
        #else weinsert it tothe right
        else:
            root.right = self._insert_bst(root.right, title_obj, key_field)
        return root
    #this is used to search for the bst
    def _search_bst(self, root, key):
        """Search BST for exact match"""
        #if there is no root then it returns a none
        if not root:
            return None
        #this is used to check if the keyis a string and thenreturn it all with a lowercase
        if isinstance(key, str):
            key = key.lower()
        #if the key is equall to the root key then we return the title object
        if key == root.key:
            return root.title_obj
        #if it is lesserwe return to the left
        elif key < root.key:
            return self._search_bst(root.left, key)
        #if it is greater we return to the right
        else:
            return self._search_bst(root.right, key)
    #this is used to get the height of the tree
    # AVL Tree operations
    def _height(self, node):
        if not node:
            return 0
        #this will self update the height
        return node.height
    #this will be used to get the height differenceon the left and right
    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    #this is used to rotate to the right side
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        
        return x
    #this is used to rotate to the left side
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y
    #this is used to insert into the avl tree
    def _insert_avl(self, root, title_obj, key_field):
        """Insert a title into AVL tree and maintain balance"""
        #if not the root then we return the avl tree
        if not root:
            return AVLNode(title_obj, key_field)
        #we have to get the atribute of the title and will automatically generate the key field
        
        key = getattr(title_obj, key_field)
        #this will convert to a lower case  if the key is a string
        if isinstance(key, str):
            key = key.lower()
        #this willl be used to insert to the left
        if key < root.key:
            root.left = self._insert_avl(root.left, title_obj, key_field)
        #this will be used to insert tothe right of the root
        else:
            root.right = self._insert_avl(root.right, title_obj, key_field)
        #this isused to update the height
        
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        #this is used to get the balance
        
        balance = self._balance_factor(root)
        
        # Left Left Case
        #this is used to rotate the key to the right
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)
        
        # Right Right Case
        #this is used to rotate to the left
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)
        
        # Left Right Case
        #this is used to rotate to the left then right
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        
        # Right Left Case
        #this is used to rotate to theright then left
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        #the whole root is returned
        
        return root
    
    # Binary Search on sorted list
    #this is used to search using the year
    def _binary_search_by_year(self, year):
        """Binary search on release year (requires sorted list)"""
        # First we need to sort the data by release year
        #this is a function  used to sort the data in a increasin order
        #sorting allows for sortd data in a given order
        sorted_data = sorted(self.data, key=lambda x: x.release_year)
        #this shows the starting point of the data 
        low = 0
        #this shows the end point of the data after it is sorted
        high = len(sorted_data) - 1
        #this shows an empty list
        results = []
        #this ensures that there is something it and is not empty
        while low <= high:
            #this is used to get the middle value by getting the low and high then dividing by two
            mid = (low + high) // 2
            #this is used to get the sorted data at the mid index and then getting the release year
            if sorted_data[mid].release_year == year:
                # Found a match, now find all matches (since there may be multiple)
                #this is used to append the data with the release year
                results.append(sorted_data[mid])
                # Check left side
                #this is used to return the soreted data at the left side
                left = mid - 1
                while left >= 0 and sorted_data[left].release_year == year:
                    #this is used to append the sorted data on the left to the results
                    results.append(sorted_data[left])
                    #this is used to continue moving to the left back by one
                    left -= 1
                # Check right side
                #this is used to move to the right
                right = mid + 1
                #thie ieusedto look at the right hand side and add the values at the right hand side
                while right < len(sorted_data) and sorted_data[right].release_year == year:
                    #this is used to append the results data on the right
                    results.append(sorted_data[right])
                    #this is used to move to the right by one
                    right += 1
                #this is used to return the results
                return results
            #this is used to  get to the left or right after checking for the left and right
            elif sorted_data[mid].release_year < year:
                low = mid + 1
            else:
                high = mid - 1
        #this is used to return the results
        return results
    
    # Public search methods
    #this is used to search for the exact title
    def exact_title_search(self, title):
        """Search for exact title match using BST"""
        #this will return the bst searchfunction
        return self._search_bst(self.title_tree, title)
    #this is used to search for the year range
    def year_range_search(self, start_year, end_year):
        """Search for titles within a year range using AVL tree"""
        #this will used to store to the list results the year tree start end and results
        results = []
        self._in_order_range_search(self.year_tree, start_year, end_year, results)
        #this will be used to return back the results function
        return results
    #this is an inorder transveral type
    def _in_order_range_search(self, node, start, end, results):
        """In-order traversal for range search"""
        #if not node we return nothing
        if not node:
            return
        #this is used to search for the left node fromthe start toend then results
        #the node.key is only accesed when it is greater hence search to the left
        if node.key > start:
            self._in_order_range_search(node.left, start, end, results)
        #this is used to search when it is greater  than the strt and and lesser to the end 
        #we then append
        if start <= node.key <= end:
            results.append(node.title_obj)
        #we will check if it is lesser than the end then we return to the right
        if node.key < end:
            self._in_order_range_search(node.right, start, end, results)
    
    #we will then search by the field 
    def search_by_field(self, term, field):
        """Linear search through all titles for partial matches in a field"""
        #we will have a results which we will use to appen
        results = []
        #we will make the term to be an all lower
        term = term.lower()
        #we will get the titees i the self.data
        for title in self.data:
            #this is used to get the title and field and convert it to a lower case
            field_value = getattr(title, field, '').lower()
            #this is used to compare the term to the field_value
            if term in field_value:
                #we will then append the title
                results.append(title)
        #we will return thewhole results
        return results
    #thus is used to get the x rated movies
    def search_x_rated(self):
        """Search for X-rated content"""
        #this will be used to store the list of results
        results = []
        #we will check each title
        for title in self.data:
            #we will check the title ratings
            if title.rating.lower() in ['x', 'nc-17']:
                #we will then append the title
                results.append(title)
        #we will return the results
        return results

# Usage Example
#this runsonly when the  code is executed directly and does not run if imported
if __name__ == "__main__":
    # Initialize the search system
    netflix = NetflixSearchSystem("/home/stevemose/data-structures-Playground/netflix_titles.csv")
    
    # 1. Exact title search using BST
    #this is used to print out the exact search 
    print("Exact title search:")
    result = netflix.exact_title_search("The Crown")
    #if the results is found then the code returns the exact search
    if result:
        print(f"Found: {result}")
        #if not found then the code prints out the title not found
    else:
        print("Title not found")
    
    # 2. Year range search using AVL tree
    #this is used to search for the year range which accepts the start and the end
    print("\nMovies between 2010 and 2012:")
    for title in netflix.year_range_search(2010, 2012):
        print(title)
    
    # 3. Binary search by exact year
    #this is used to search by the year
    print("\nMovies from 2010 (using binary search):")
    for title in netflix._binary_search_by_year(2010):
        print(title)
    
    # 4. Search by field (linear search)
    #this is used to search by the field 
    print("\nCrime shows:")
    for title in netflix.search_by_field('crime', 'listed_in'):
        print(title)
    
    # 5. X-rated content search
    #this is used to search for the x rated content
    print("\nX-rated content:")
    for title in netflix.search_x_rated():
        print(f"{title.title} ({title.rating})")