class LRUCache(object):
    # tc : O(1) to get, put
    # sc : O(n) where n is the capacity
    # intution 
    # is to abel to get and put in O(1), so the idea is to whenever we call get we put that item on the front of the list-> indicating recentlyused,
    # and when put is called and if capacity excceds then we remove the last element as it is least recently used, and insert the element at the front
    # to easily move the data from x position to the front, its easy if we use double linked list
    # as double linked list , we have the prev and next so its easy to break the connection there and move it to the front 
    #  Will also have a hashmap to store each key node, so that search is also O(1)
    
    class Node:
        def __init__(self,key,val):
            # since we have key and value pairs we will have variables for key and value
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.hash_map = {} # to make search get function in O(1)
        self.capacity = capacity
        # setting intial head and tail of the double linked lists
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodetoHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node

    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    

    def get(self, key):
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        # remove the node there and put it in the front
        self.removeNode(node)
        self.addNodetoHead(node)
        return node.val


    def put(self, key, value):
        # if the key exists change its value
        if key in self.hash_map:
            # find the node 
            node = self.hash_map[key]
            # change its value
            node.val = value

            # remove node at that position
            self.removeNode(node)

            # place it in the front 
            self.addNodetoHead(node)
        
        # if not there two things, check the capacity, then find the least recently used 
        else:
            if len(self.hash_map) == self.capacity:
                # least recently used is the last node , remove it 
                lastnode = self.tail.prev 
                # remove the this node in double linked list
                self.removeNode(lastnode)
                # also remove it from the hashmap as well 
                del self.hash_map[lastnode.key]
            # add the new node
            newnode = self.Node(key,value)
            self.addNodetoHead(newnode)
            self.hash_map[key] = newnode
