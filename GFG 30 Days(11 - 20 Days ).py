#In[11]

Secret Cipher

Geek wants to send an encrypted message in the form of string S to his friend Keeg along with instructions on how to decipher the message. To decipher the message, his friend needs to iterate over the message string from left to right, if he finds a '*', he must remove it and add all the letters read so far to the string. He must keep on doing this till he gets rid of all the '*'.
Can you help Geek encrypt his message string S? 

Note: If the string can be encrypted in multiple ways, find the smallest encrypted string. 

class Solution:
    def fillarray(self, s, a):
        a[0]=0
        for i in range(1,len(s)):
            series=a[i-1]
            while(series):
                if(s[series]==s[i]):
                    a[i]=series+1
                    break
                series=a[series-1]
            if(series==0):
                a[i]=(int(s[i]==s[0]))
        return a
        
    def compress(self, s):
        a=[0]*len(s)
        
        #  ith element of array a stores the length of longest
        #  proper suffix which is also a proper prefix
        #  for substr s[0] to s[i]
        a = self.fillarray(s, a)
        #print(a)
        shortened=[]
        n=len(s)
        i=n-1
        
        #  for even index, string length is odd
        #  hence it cannot be divided into two
        #  so we simply push ith character in stack
        while(i>0):
            if(i%2==0):
                shortened.append(s[i])
                i=i-1
                continue
            
            # star_here will be made TRUE if substring s[0] to s[i]
            # can be divided into identical halves
            star_here=False
            
            #  suffix and substring length are also meant for
            #  substring s[0] to s[i]
            suffix=a[i]
            substrlen=i+1
            
            #  these conditions, if true, imply that, substring
            #  can be divided into 2 identical halves
            if(suffix*2>=substrlen):
                if(substrlen%(substrlen-suffix)==0):
                    if((substrlen/(substrlen-suffix))%2==0):
                        star_here=True
                        
            
            #  adding * to stack and moving index as required
            if(star_here==True):
                shortened.append('*')
                i=(i//2)+1
                
            #  else, simply adding character to stack
            else:
                shortened.append(s[i])
            i=i-1
        ret=""
        ret=ret+s[0]
        n=len(shortened)
        
        #  since we analysed input string from end to start
        #  removing elements from stack and pushing back to
        #  output string will reverse them back to required order
        while(n):
            ret=ret+shortened[n-1]
            shortened.pop()
            n=n-1
        return ret
    
#In[12]


Check Tree Traversal

Given Preorder, Inorder and Postorder traversals of some tree of size N. The task is to check if they are all of the same tree or not.
    
    
    
   Given an integer array of size  N . You have to find sum of bit differences in all pairs that can be formed from array elements. 
    Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.
    For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers). 
    
            class Solution:
                def sumBitDiff(self, arr, n): 
                    # Your code goes here
                    ans = 0
                    for i in range(0,32):
                        count = 0
                        for j in range(0,n):
                             if ( (arr[j] & (1 << i)) ): 
                                count+=1

                        # Add "count * (n - count) * 2" to the answer 
                        ans += (count * (n - count) * 2); 

                    return ans
                
                
   #In[13]             
                
            
            
            class Solution:
                def checktree(self, preorder, inorder, postorder, N): 


                    if N == 0: 
                        return 1

                    if N == 1: 
                        return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0]); 

                    idx = -1; 

                    for i in range(N): 
                        if inorder[i] == preorder[0]: 
                            idx = i 
                            break

                    if idx == -1: 
                        return 0;

                    if preorder[0] != postorder[N-1]:
                        return 0;


                    ret1 = self.checktree(preorder[1:], inorder, postorder, idx); 

                    ret2 = self.checktree(preorder[idx + 1:], inorder[idx + 1:], 
                                        postorder[idx:], N-idx-1); 

                    return (ret1 and ret2) 



