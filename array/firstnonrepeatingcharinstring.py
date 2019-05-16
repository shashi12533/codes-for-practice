https://www.geeksforgeeks.org/first-non-repeating-character-using-one-traversal-of-string-set-2/

import math as mt 
  
NO_OF_CHARS = 256
  
''' 
The function returns index of the first  
non-repeating character in a string. If  
all characters are repeating then  
reurns INT_MAX '''
  
def firstNonRepeating(strng): 
    #initialize all character as absent 
      
    arr=[-1 for i in range(NO_OF_CHARS)] 
      
    ''' 
    After below loop, the value of  
    arr[x] is going to be index of  
    of x if x appears only once. Else  
    the value is going to be either  
    -1 or -2.'''
      
    for i in range(len(strng)): 
        if arr[ord(strng[i])]==-1: 
            arr[ord(strng[i])]=i 
        else: 
            arr[ord(strng[i])]=-2
    res=10**18
      
    for i in range(NO_OF_CHARS): 
        ''' 
        If this character occurs only  
        once and appears before the  
        current result, then update the  
        result'''
        if arr[i]>=0: 
            res=min(res,arr[i]) 
    return res 
  
#Driver prohram to test above function 
  
strng="geeksforgeeks"
  
index=firstNonRepeating(strng) 
  
if index==10**18: 
    print("Either all characters are repeating or string is empty") 
else: 
    print("First non-repeating character is",strng[index]) 
  
def FirstRepeated(string): 
      
    # An integer to store presence/absence 
    # of 26 characters using its 32 bits. 
    checker = 0
   
    pos = 0
    for i in string: 
        val = ord(i) - ord('a'); 
   
        # If bit corresponding to current 
        # character is already set 
        if ((checker & (1 << val)) > 0): 
            return pos 
   
        # set bit in checker 
        checker |= (1 << val) 
        pos += 1
   
    return -1
   
# Driver code 
string = "abcfdeacf"
i = FirstRepeated(string) 
if i != -1: 
    print "Char = ", string[i], " and Index = ", i; 
else: 
    print "No repeated Char"
  
# This code is contributed by Sachin Bisht 
      








