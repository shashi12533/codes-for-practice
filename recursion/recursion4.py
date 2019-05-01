https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/


def printCombination(arr, n, r,m):
    data = [0] * r

    combinationUtil(arr, n, r, 0, data, 0,m)


def combinationUtil(arr, n, r, index, data, i,m):

    if (index == r):
        if sum(data)%m==0:
            print(data)
        print()
        return


    if (i >= n):
        return


    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1,m)


    combinationUtil(arr, n, r, index,
                    data, i + 1,m)


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    r = 3
    n = len(arr)
    m=3
    printCombination(arr, n, r,m)

# This code is contributed
# by ChitraNayal
