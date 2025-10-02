# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """


#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    # tc : O(1) for next and hasnext 
    # sc : O(d) space taken by the recrussive stack : where d is the depth of the nested lists 
    # ran successfuly on leetcode

    # intution 
    # brute force : flatten the iterator and sva ethe lements as interner and for next just pop the integre, and for has next if there are elements in the queue then we can say hasnext is True
    # drawback of this : its memory inefficient we are svaing all the elemenst not kknowing if we are gng to cll next or hasnexct those many times, if there is any new data cmg into the iterator or remove the a data, the method returns the old data output only which is wrong
    # efficient approach : doing lazy loading, for data sturture we will use the iterator object only 

    def __init__(self, nestedList):
        self.stack = [iter(nestedList)] # stack of the nestediterator
        self.nextEl = 0 #intially setting the next element as 0 will be overwritten latter in the function

    def next(self):
        return self.nextEl.getInteger() # return the interger of the next element

    def hasNext(self):
        # we will keep iteratign each element and the peek element we will put it on the top of the stack and return the integer from this top element
        # once this iterator is empty we just pop it up and then process the next element in the nested list , keep doing the proces where we keep movign one step ahead and put
        # take the peek element convert to iterator and out in on the top and process so on un til we reach end of the list 
        
        while self.stack:
            self.nextEl = next(self.stack[-1], None) # stack[-1] takes the peek element, and returns the integer if ntg there then returns none
            if self.nextEl is None: # the iterator is exhausted we pop it up and move to next element in the nested iterator and check until the staxck is not empty 
               self.stack.pop()
            else: # its not none, 
                if self.nextEl.isInteger(): # check if the element is integer then it has next return True
                    return True
                else :
                    # its not an integer but a list, 
                    # get the list from the next el : self.nextEl.getList() , change to iter and then append 
                    self.stack.append(iter(self.nextEl.getList()))

        return False # if stack was empty then there is no more hasnetx return he false 

    






        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())