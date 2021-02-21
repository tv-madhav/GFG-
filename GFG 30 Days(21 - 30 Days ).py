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
    
    
    
    #In[23]
    
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
    
    
    
  #In[25]

 Spidey Sense 

Spiderman is stuck in a difficult situation. His arch-enemy the Green Goblin has planted several of his infamous Pumpkin Bombs in 
various locations in a building. Help Spiderman activate his Spidey Sense and identify the impact zones. 
He has a blueprint of the building which is a M x N matrix that is filled with the characters ‘O’, ‘B’, and ‘W’ where: 
‘O’ represents an open space.
‘B’ represents a bomb.
‘W’ represents a wall.
You have to replace all of the O’s (open spaces) in the matrix with their shortest distance from a bomb without being able to go 
through any walls. Also, replace the bombs with 0 and walls with -1 in the resultant matrix. If no path exists between a bomb and an 
open space replace the corresponding 'O' with -1.


    
from collections import deque

dr = [-1,0,0,1]
dc = [0,-1,1,0]
class Solution:
    def findDistance(self, matrix, m, n):
        # Your code goes here
        ret = [ [-1 for _ in range(n)] for _ in range(m) ]
        q = deque()
    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'B':
                    ret[i][j] = 0
                    q.append((i,j))
    
        while len(q):
            r=q[0][0]
            c=q[0][1]
            q.popleft()
    
            for i in range(4):
                nextr=r+dr[i]
                nextc=c+dc[i]
                if nextr>=0 and nextr<m and nextc>=0 and nextc<n:
                    if ret[nextr][nextc]==-1 and matrix[nextr][nextc]=='O':
                        ret[nextr][nextc] = ret[r][c]+1
                        q.append((nextr,nextc))
        return ret
        
        
        
        
     #In[26]
    
    Project Manager 
   
   An IT company is working on a large project. The project is broken into N modules and distributed to different teams. 
    The amount of time (in months) required to complete each module is given in an array duration[ ]. Two modules can be processed simultaneously 
    only if their is no dependency between them and it is given that M modules have interdependecies. 
    As the project manager, compute the minimum time required to complete the project. 
    

from collections import defaultdict

class Solution:
    def checkCycle(self, i):
        global isstack
        global visited
        global counted
        global ve
        if (isstack[i] == 1):
            return rue
        # insert into stack
        isstack[i] = 1
        for it in ve[i]:
            # if next node is visited
            if (visited[it] == 1):
                # if the node is in stack then cycle is found
                if (isstack[it] == 1):
                    return True
                continue
            visited[it] = 1
            if (self.checkCycle(it)==True):
                return True;
        # removing from stack   
        isstack[i] = 0
        return False
    
    def dfs(self, i, duration):
        global counted
        global visited
        global isstack
        global ve
        #  return the time to complete the project starting from the node i if it is
        #  already calculated
        if (counted[i] != -1):
            return counted[i]
        x = 0;
    
        for it in ve[i]:
            x = max(x, self.dfs(it, duration))
        #  time to complete this module and maximum time to complete child modules
        counted[i] = x + duration[i]
        return counted[i]
    
    def minTime(self, vp, duration, n, m):
        independent=[0]*(n+5)
        global ve
        ve = defaultdict(lambda:[])
        for i in range(0,m):
            x = vp[i][0]
            y = vp[i][1]
            ve[x].append(y)
            independent[y]+=1
        global visited
        global counted
        global isstack
        visited =[-1]*(n+5)
        counted =[-1]*(n+5)
        isstack =[-1]*(n+5)
        
        flag = 0;
        for i in range(0,n):
            if (independent[i] == 0):
                flag = 1
        # no independent module
        if (flag == 0):
            return -1
    
        for i in range(0,n):
            if (independent[i] != 0):
                continue
            visited[i] = 1
            # checking cycle 
            if (self.checkCycle(i)):
                return -1
        
        ans = 0;
        # starting from any independent module find the maximum time to complete
        # the project
        for i in range(0,n):
            if (independent[i] == 0):
                ans = max(ans, self.dfs(i, duration));
    
        return ans
    
    
#In[26]

Police and Thives

Given an array of size n such that each element contains either a 'P' for policeman or a 'T' for thief. Find the maximum number of thieves that can be caught by the police. 
Keep in mind the following conditions :

Each policeman can catch only one thief.
A policeman cannot catch a thief who is more than K units away from him.
    
    
    
class Solution:
    def catchThieves(self, arr, n, k): 
        # code here 
        i = 0
        l = 0
        r = 0
        result = 0
        thief = []
        police = []
        while i < n :
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thief.append(i)
            i += 1
            
        while l < len(thief) and r < len(police):
            if (abs(thief[l] - police[r]) <= k):
                result +=1
                l += 1
                r += 1
                
            elif thief[l] < police[r]:
                l += 1
            else:
                r +=1
                
        return result
