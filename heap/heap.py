#!/usr/bin/python

# This heap class start from here.
class Heap:
    def __init__(self):  # Default constructor of heap class.
        self.h = []
        self.currsize = 0


    def maxHeapify(self,i):
        parent=i
        left = i*2
        right = i*2+1
        if left<self.currsize and self.h[left]>self.h[parent]:
           parent=left
        if right<self.currsize and self.h[right]>self.h[parent]:
            parent=right

        # this code below is written because parent index value has to be swapped if it doesn't satisfy max heap property otherwise ignore
        if parent!=i:
            self.h[i],self.h[parent] = self.h[parent],self.h[i]
            self.maxHeapify(parent)

    def getmax(self):
        print(self.h)
        return self.h[0]


    def insert(self,k):
        self.h.append(k)
        curr = self.currsize
        self.currsize=self.currsize+1
        while self.h[curr]>self.h[curr//2]:
            self.h[curr],self.h[curr//2]= self.h[curr//2],self.h[curr]
            curr=curr//2
    def delete(self):
        m= self.h[0]
        n= self.h[len(self.h)-1]
        self.h[0],self.h[len(self.h)-1] = self.h[len(self.h)-1],self.h[0]
        self.h.pop()
        self.currsize=self.currsize-1
        self.maxHeapify(0)
        print(self.h)









    def buildHeap(self,l):
        self.currsize= len(l)
        self.h=l
        for i in range(self.currsize//2,-1,-1):
            self.maxHeapify(i)




def main():
    #l = list(map(int, input().split()))
    l=[1,2444,3,4,5,6]
    h = Heap()
    h.buildHeap(l)
    h.insert(44444)
    print(h.getmax())
    h.delete()
    # h.heapSort()
    # h.display()


if __name__ == "__main__":
    main()

