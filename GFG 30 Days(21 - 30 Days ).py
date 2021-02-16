#In[21]

Corona Vaccine

Geek has developed an effective vaccine for Corona virus and he wants each of the N houses in Geek Land to have access to it. 
Given a binary tree where each node represents a house in Geek Land, find the minimum number of houses that should 
be supplied with the vaccine kit if one vaccine kit is sufficient for that house, its parent house and it's immediate child nodes.  


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''

class Solution:
    def traverse(self, n):
        if not n:
            return (0,2)
        
        vaccineKitL , distL = self.traverse(n.left)
        vaccineKitR , distR = self.traverse(n.right)
        
        if max(distL,distR) == 3:
            return (vaccineKitL+vaccineKitR+1 , 1)
        
        return ( vaccineKitL+vaccineKitR , 1+min(distL,distR) )

    def supplyVaccine(self, root):
        vaccineKit,dist = self.traverse(root)
        if dist==3:
            return vaccineKit+1
        return vaccineKit


