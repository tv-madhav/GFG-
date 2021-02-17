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
    
    
 #In[22]


Shortest Range In BST 

Given a BST (Binary Search Tree), find the shortest range [x, y], such that, at least one node of every level of the BST lies in the range.
If there are multiple ranges with the same gap (i.e. (y-x)) return the range with the smallest x.

class Solution:
    
    def storein(self, root, lvl, lin, llv):
        if not root:
            return
        self.storein(root.left,lvl+1,lin,llv)
        lin.append(root.data)
        llv.append(lvl)
        self.storein(root.right,lvl+1,lin,llv)
        
        
        
    def shortestRange(self, root):

        inorder=[]
        level=[]
        self.storein(root,0,inorder,level)
        i=j=k=cntzero=0
        maxDepth=max(level)+1
        #  stores number of nodes at ith level
        depth=[0]*maxDepth
        # first count number of nodes at ith level till the root 
        #  right pointer initially is at root's index in inorder traversal of bst
        for k in range(len(level)):
            depth[level[k]]+=1
            if level[k]==0:
                j=k
                break
        #  count number of levels where there are 0 nodes in the range inorder[i] to inorder[j]
        cntzero=depth.count(0)
        #  intially shortest range is [x, y]
        #  x=node at 0th index
        #  y=node at last index
        #  i.e. the whole tree
        x,y=inorder[0],inorder[-1]
        # if currently picked range contains all levels change x and y accordingly
        if cntzero==0:
            x,y=inorder[i],inorder[j]
    
        # left pointer can at most go upto root's index(i.e. k)
        # right pointer can go upto last index of inorder traversal of tree
        while i<=k and j<len(inorder):
            #  while right pointer doesn't reach last index 
            #  and the current range doesn't contain all levels
            while j<len(inorder):
                #  if cntZero is 0 then this range contains all levels
                if cntzero==0:
                    #  if previous range is large then change the range
                    if (y-x) > (inorder[j]-inorder[i]):
                        x,y=inorder[i],inorder[j]
                    break
                j+=1
    
                if j>= len(inorder):
                    break
                #  if new level is discovered by this range then cntZero is decreased by 1
                if depth[level[j]]==0:
                    cntzero-=1
                depth[level[j]]+=1
            #  while current range contains all levels 
            # we can shift the left pointer by +1
            while not cntzero and i<=k:
                if (y-x)>(inorder[j]-inorder[i]):
                    x,y=inorder[i],inorder[j]
                depth[level[i]]-=1
                #  if this level is outside the current range then cntZero is increased by 1
                if depth[level[i]]==0:
                    cntzero+=1
                i+=1
        return (x,y)
    
    
    
    #In[22]
    
    Lucy's Neighbours

        Lucy lives in house number X. She has a list of N house numbers in the society. Distance between houses can be determined by studying the difference between house numbers. 
        Help her find out K's closest neighbors.
        Note: If two houses are equidistant and Lucy has to pick only one, the house with the smaller house number is given preference.

class Solution:
    def Kclosest(self, arr, n, x, k):
        # Your code goes here
        max_heap = [ ( -1*abs(x-arr[i]) , -1*arr[i] ) for i in range(k) ]
        heapq.heapify(max_heap)
        for i in range(k,n):
            dist = -1*max_heap[0][0]
            hno  = -1*max_heap[0][1]
            if abs(arr[i]-x)<dist or ( abs(arr[i]-x)==dist and arr[i]<hno ):
                heapq.heappop(max_heap)
                heapq.heappush( max_heap, ( -1*abs(x-arr[i]) , -1*arr[i] ) )
        
        ret=[ -1*x[1] for x in max_heap]
        ret.sort()
        return ret
