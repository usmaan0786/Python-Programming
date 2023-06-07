from asyncio.windows_events import NULL
from http.client import FOUND
#from logging import _Level
from operator import truediv
from tkinter.tix import Tree
from turtle import left

from numpy import equal


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
    
    def num_of_nodes(self, n):
        if self == None:
            return 0
        print(self.val,n)
        if self.left is not None:
            n = self.left.num_of_nodes(n+1)
        if self.right is not None:
            n = self.right.num_of_nodes(n+1)
        return n
       
    def search(self, key):
        if self == None:
            return False
        if self.val == key:
            return True
        if self.val > key and self.left is not None :
            return self.left.search(key)
        if self.val < key and self.right is not None:
            return self.right.search(key)

#    def height(self):
#        if self is None:
#            return 0
#        left_height = self.left.height()
#        right_height = self.right.height()
#
#        max_height = left_height
#        if right_height > max_height:
#            max_height = right_height
#        return max_height + 1



    def height(self):
        if self is None:
            return 0

        if self.left is not None:
            ldepth = self.left.height()
        else:
            ldepth = -1
             
        if self.right is not None:
            rdepth = self.right.height()
        else:
            rdepth = -1

        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth+1

    def depth_of_node(self, val, h = 0):
        if self is None:
            return 0
        if self.val == val:
            return h
        if val < self.val and self.left is not None:
            return self.left.depth_of_node(val, h + 1)
        if val > self.val and self.right is not None:
            return self.right.depth_of_node(val, h + 1)
        

    def depth_limited_search(self, val, limit, h = 0):
        if self is None:
            return 0
        if self.val == val:
            return True
        if h < limit:
            if val < self.val and self.left is not None:
                return self.left.depth_limited_search(val, limit, h + 1)
            if val > self.val and self.right is not None:
                return self.right.depth_limited_search(val, limit, h + 1)
        else:
            print("Value not Found in given Limit")
            return False
        


if __name__ == '__main__':
    #nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24]
    nums = [12, 6, 4, 1, 9, 18, 15, 30, 13, 14]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
print("preorder:")
print(bst.preorder([]))
#print("num of nodes = ", bst.num_of_nodes(1))
#print("Value Found = ", bst.search(3))
#print(bst.depth_of_node(14))
print(bst.depth_limited_search(14, 4))