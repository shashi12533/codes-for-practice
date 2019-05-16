def findPlatform(arr,dep,n): 
  
    # Sort arrival and 
    # departure arrays 
    arr.sort() 
    dep.sort() 
   
    # plat_needed indicates 
    # number of platforms 
    # needed at a time 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
   
    # Similar to merge in 
    # merge sort to process  
    # all events in sorted order 
    while (i < n and j < n): 
     
        # If next event in sorted 
        # order is arrival,  
        # increment count of 
        # platforms needed 
        if (arr[i] < dep[j]): 
          
            plat_needed+=1
            i+=1
   
            # Update result if needed  
            if (plat_needed > result):  
                result = plat_needed 
          
   
        # Else decrement count 
        # of platforms needed 
        else: 
          
            plat_needed-=1
            j+=1
          
    return result 
  
# driver code 
  
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 
  
print("Minimum Number of Platforms Required = ", 
        findPlatform(arr, dep, n)) 











#include <bits/stdc++.h> 
using namespace std; 
  
int findPlatform(int arr[], int dep[], int n) 
{ 
    // Insert all the times (arr. and dep.) 
    // in the multimap. 
    multimap<int, char> order; 
    for (int i = 0; i < n; i++) { 
  
        // If its arrival then second value 
        // of pair is 'a' else 'd' 
        order.insert(make_pair(arr[i], 'a')); 
        order.insert(make_pair(dep[i], 'd')); 
    } 
  
    int result = 0; 
    int plat_needed = 0; 
  
    multimap<int, char>::iterator it = order.begin(); 
  
    // Start iterating the multimap. 
    for (; it != order.end(); it++) { 
  
        // If its 'a' then add 1 to plat_needed 
        // else minus 1 from plat_needed. 
        if ((*it).second == 'a') 
            plat_needed++; 
        else
            plat_needed--; 
  
        if (plat_needed>result) 
            result = plat_needed; 
    } 
    return result; 
} 
  
// Driver code 
int main() 
{ 
    int arr[] = { 900, 940, 950, 1100, 1500, 1800 }; 
    int dep[] = { 910, 1200, 1120, 1130, 1900, 2000 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    cout << "Minimum Number of Platforms Required = "
         << findPlatform(arr, dep, n); 
    return 0; 
} 
