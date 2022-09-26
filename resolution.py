# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math     
     
# min-heap class type
class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0
        
    def getMin(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[0]
            
    def heapify(self):
        if self.size == 0:
            return
            
        #for all the non leaf node
        nonLeaf = math.floor(((self.size)/2)-1)
        if nonLeaf < 0:
            nonLeaf = 0
        
        for i in range(nonLeaf,-1,-1):
            smallest = i
            minIndex = smallest
            
            leftIndex = smallest*2 + 1
            rightIndex = smallest*2 + 2
            
            
            if leftIndex < self.size and self.arr[leftIndex] < self.arr[smallest]:
                smallest = leftIndex
            if rightIndex < self.size and self.arr[rightIndex] < self.arr[smallest]:
                smallest = rightIndex
            
            #swap
            self.arr[minIndex], self.arr[smallest] = self.arr[smallest], self.arr[minIndex]
            
    def deleteIndex(self, index):
        if self.size == 0:
            return
        
        if index == self.size - 1:
            self.arr.pop()
            self.size -= 1
        else:
            #swap the index with the leaf
            lastLeaf = self.size - 1
            self.arr[lastLeaf], self.arr[index] = self.arr[index], self.arr[lastLeaf]
            self.arr.pop()
            self.size -= 1
            self.heapify()
                    
    def delete(self, value):
        valueIndex = -1
        
        try:
            valueIndex = self.arr.index(value)
        except ValueError:
            return
            
        self.deleteIndex(valueIndex)
            
    def insert(self, value):
        self.arr.append(value)
        self.size += 1
        self.heapify()        

def execQueries(n, queries):
    heap = MinHeap()
    
    for q in queries:
        
        if q[0] == "3":
            # print the minimum
            print(heap.getMin())
            continue
            
        if q[0] == "2":
            # delete the element q[2] from the heap
            heap.delete(int(q[2:]))
            continue
            
        if q[0] == "1":
            # add the element q[2] from the heap
            heap.insert(int(q[2:]))
            continue
    

# main
if __name__ == "__main__":
    queries = []
    i = 0
    
    nOfQuery = 0
    
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        if i == 0:
            i += 1
            nOfQuery = int(line.rstrip())
        else:
            queries.append(line.rstrip())
    
    execQueries(nOfQuery,queries)