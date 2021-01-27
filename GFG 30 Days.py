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

# In[ ]:
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



