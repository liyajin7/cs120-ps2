class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: string
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    # # INCORRECT by the Roughgarden algorithm!
    # def select(self, ind):
    #     left_size = 0
    #     if self.left is not None:
    #         left_size = self.left.size
    #     if ind == left_size:
    #         return self
    #     if left_size > ind and self.left is not None:
    #         return self.left.select(ind)
    #     if left_size < ind and self.right is not None:
    #         return self.right.select(ind)
    #     return None

    # CORRECT FOR CALC FOR THE RIGHT SUBTREE
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)       # changed this part: check the tests
        return None
    

    # # ROUGHGARDEN
    # def select(self, ind):
    #     left_size = 0
    #     if self.left is not None:
    #         left_size = self.left.size
    #     if ind == left_size + 1:
    #         return self
    #     if ind < left_size + 1 and self.left is not None:
    #         return self.left.select(ind)
    #     if left_size + 1 < ind and self.right is not None:
    #         return self.right.select(ind - left_size - 1)
    #     return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1
        # print(self)
        # self.calculate_sizes()
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):

        # THERE'S ONE MISTAKE IN HERE!
        
        if child_side == "L":
            top = self.left
        else: top = self.right

        if direction == "L":
            # instantiate node to be rotated "up": new top node
            new_top = top.right

            # @LIYA new: update size of top
            temp = top.size
            top.size -= new_top.size
            new_top.size += temp
            if new_top.left != None:
                top.size += new_top.left.size

            # set new_top's left subtree to previous top's right subtree
            top.right = new_top.left
            
            # set new_top to be either L or R subtree of self, depending on original child_side
            if child_side == "L":
                self.left = new_top
            else: self.right = new_top

            # set previous top to be left child of new_top
            new_top.left = top

            # new size change
            
            new_top.size

        else: 
            # instantiate node to be rotated "up": new top node
            new_top = top.left

            # @LIYA new: update size of top
            temp = top.size
            top.size -= new_top.size
            new_top.size += temp
            if new_top.right != None:
                top.size += new_top.right.size

            # turn new_top's right subtree into previous top's left subtree
            top.left = new_top.right
            
            # set new_top to be either L or R subtree of self, depending on original child_side
            if child_side == "L":
                self.left = new_top
            else: self.right = new_top

            # set previous top to be right child of new_top
            new_top.right = top

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self