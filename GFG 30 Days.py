#!/usr/bin/env python
# coding: utf-8

# In[1]:

GFG 30 Days:


Geek and his classmates are playing a prank on their Computer Science teacher. They change places every time the teacher turns to look at the blackboard. 
Each of the N students in the class can be identified by a unique roll number X and each desk has a number i associated with it. Only one student can sit on one desk. 
Each time the teacher turns her back, a student with roll number X sitting on desk number i gets up and takes the place of the student with roll number i.
If the current position of N students in the class is given to you in an array, such that i is the desk number and a[i] is the roll number of the student sitting on the desk, can you modify a[ ] to represent the next position of all the students ? 

Your Task:  
You dont need to read input or print anything. Complete the function prank() which takes the array a[ ] and its size N as input parameters and modifies the array in-place to reflect the new arrangement.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 105
0 ≤ a[i] ≤ N-1

class Solution:
    def prank( a, n): 
        n = len(a)
        for i in range (n):
            a[i] = a[i] + (a[a[i]]%n)*n
        for i in range (n) :
            a[i] = int(a[i]/n)
        return(a)

# In[2 ]:
Nth Natural Number
Given a positive integer N. You have to find Nth natural number after removing all the numbers containing digit 9 .

class Solution:
    def findNth(self,N):
        #code here
        a = ""
        while(N):
            a = str(N%9) + a
            N = N//9
        return int(a)
       
       
  #IN[3 ]:
  
   Smallest Positive Integer that can not be represented as Sum
  Given an array of size N, find the smallest positive integer value that cannot be represented as sum of some elements from the array.
  
  class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
        ans = 1
        array.sort()
        for i in range(n):
            if (array[i] <= ans):
                ans = ans + array[i]
        return ans
                
     #IN[4]:
     
     Number of minimum picks to get 'k' pairs of socks from a drawer
     A drawer contains socks of n different colours. The number of socks available of ith colour is given by a[i] where a is an array of n elements. 
     Tony wants to take k pairs of socks out of the drawer. However, he cannot see the colour of the sock that he is picking. You have to tell what is 
     the minimum number of socks Tony has to pick in one attempt from the drawer such that he can be absolutely sure, without seeing their colours, 
     that he will have at least k matching pairs.
     
     

class Solution:
    def find_min(self, a, n, k):
        #Code Here
        sock = 0
        total_pairs = 0
        for i in range(0,n):
            total_pairs += a[i]//2;
            
            if ( a[i] % 2 == 0):
                sock += (a[i]-2)//2;
            else:
                sock += (a[i] -1)//2;
        if (k > total_pairs):
            return -1;
        if (k <= sock):
            return 2*(k-1) + n + 1;
            
        return 2*sock + n + (k-sock);
       
       
      #In[5]
      
  Spiral Matrix
  Given a matrix of size N x M. You have to find the Kth element which will obtain while traversing the matrix spirally starting from the top-left corner of the matrix.
  
    class Solution:
      def Spiral_matrix:
      
        top = 0
        left = 0
        right = m-1;
        bottom = n-1;
        dir =0;
        count=0;
        while(top<=bottom and left<=right):
            if(dir==0):
                for i in range(left, right+1):
                    k -= 1
                    if k == 0:
                        return (a[top][i])
                top += 1
                dir=1
                    
            if(dir==1):
                for i in range(top, bottom+1):
                    k -= 1
                    if k == 0:
                        return (a[i][right])
                right -= 1
                dir=2
            if(dir==2):
                for i in range(right, left - 1, -1):
                    k -= 1
                    if k == 0:
                        return (a[bottom][i])
                bottom -= 1
                dir=3
            if(dir==3):
                for i in range(bottom, top - 1, -1):
                    k -= 1
                    if k == 0:
                        return (a[i][left])
                left += 1
                dir=0

            

 #In[6]
 Coins of Geekland
 
 In Geekland there is a grid of coins of size N x N. You have to find the maximum sum of coins in any sub-grid of size K x K.
Note: Coins of the negative denomination are also possible at Geekland.
 
 class Solution:
    def Maximum_Sum(self, mat, N, K):
        # Your code goes here
        sum_mat = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for a in range(N):
                sum_mat[i][a] = mat[i][a]
                if i>0:
                    sum_mat[i][a] += sum_mat[i-1][a]
                if a >0:
                    sum_mat[i][a] += sum_mat[i][a-1]
                if i >0 and a >0:
                    sum_mat[i][a] -= sum_mat[i-1][a-1]
        r=0
        for i in range(K-1,N):
            for a in range(K-1,N):
                value = sum_mat[i][a]
                if i>K-1:
                    value -= sum_mat[i-K][a]
                if a >K-1:
                    value -= sum_mat[i][a-K]
                if i >K-1 and a>K-1:
                    value += sum_mat[i-K][a-K]
                    
                r = max(r, value)
                
        return r
                
            
 #In[7]
  Valid Pair Sum
 
 Given an array of size N, find the number of distinct pairs {a[i], a[j]} (i != j) in the array with their sum greater than 0.
       from bisect import bisect_left as lower_bound
       class Solution:
           def ValidPair(self, a, n): 
            # Your code goes here
            a = sorted(a)
            res = 0
            for i in range(n):
                if (a[i]<=0):
                    continue
                j = lower_bound(a,-a[i] + 1) 
             res += i - j 
            return res 
           
           
      #In[8]   
      
      Dam of Candies
           
      Geek wants to make a special space for candies on his bookshelf. Currently, it has N books of different heights and unit width. 
      Help him select 2 books such that he can store maximum candies between them by removing all the other books from between the selected books. 
      The task is to find out the area between 2 books that can hold the maximum candies without changing the original position of selected books.      
           
     class Solution:
           def maxCandy(self, height, n): 
               # Your code goes here
               # two pointers
               maximum = 0
               a = 0
               b = n-1
               while(a<b):
                   if (height[a]<height[b]):
                       maximum = max(maximum, (b-a-1)*height[a])
                       a += 1
                   elif(height[a]>height[b]):
                        maximum = max(maximum, (b-a-1)*height[b])
                        b -= 1
                   else:
                       maximum = max(maximum, (b-a-1)*height[a])
                       a += 1
                       b -= 1

               return maximum
              
         #In[9]           
              
              
      Transfiguration         
              
  Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the 
  trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string,
  remove it and insert it in the beginning. 
  Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.          
  
  
    class Solution:
      def transfigure(self, A, B): 
          # code here 
          a = len(A)
          b = len(B)
          if b != a:
              return -1
          count = {}
          keys = count.keys()
          for i in A:
              if i in keys:
                  count[i] += 1
              else:
                  count[i] = 1
          for i in B:
              if i in keys:
                  count[i] -= 1
              else:
                  count[i] = 1
          for i in keys:
              if count[i]:
                  return -1
          ans = 0
          i = b-1
          j = b-1
          while i >= 0:
              while i>=0  and A[i] != B[j]: 
                  i -= 1
                  ans += 1

              # if A[i] and B[j] match 
              if i >= 0: 
                  i -= 1
                  j -= 1

          return ans

 #In[10]     
         
       Repeated String Match
   
       Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A. 
        If B cannot be a substring of A no matter how many times it is repeated, return -1. 
         class Solution:
             def repeatedStringMatch(self, A, B):
                 # code here
                 a = A
                 ans = 1
                 while len(a)<len(B):
                     a +=A
                     ans +=1
                 if B in a:
                     return ans
                 if B in a + A :
                     return ans + 1
                 return -1
