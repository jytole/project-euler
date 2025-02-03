import math

class Node(object):
        nodeID = -1
        key = -1
        
        def __init__(self, nodeID, key):
            self.nodeID = nodeID
            self.key = key

class dijkstraHeap(object):
    heap = []

    def __init__(self, heap):
        self.heap = heap

    def bubbleUp(self, idx):
        while(idx > 0):
            parentIdx = math.floor((idx - 1) / 2)
            if(self.heap[idx].key > self.heap[parentIdx].key):
                tmp = self.heap[idx]
                self.heap[idx] = self.heap[parentIdx]
                self.heap[parentIdx] = tmp
                idx = parentIdx
            else:
                return
    def bubbleDown(self, idx):
        while idx < math.floor(len(self.heap) / 2):
            leftIdx = idx * 2 + 1
            rightIdx = idx * 2 + 2
            if(self.heap[leftIdx].key > self.heap[rightIdx].key):
                if(self.heap[leftIdx].key > self.heap[idx].key):
                    # left is max, swap left and idx, follow idx down
                    tmp = self.heap[leftIdx]
                    self.heap[leftIdx] = self.heap[idx]
                    self.heap[idx] = tmp
                    idx = leftIdx
                else:
                    return
            elif(self.heap[rightIdx].key > self.heap[idx].key):
                # right is max, swap right to idx, follow idx down
                tmp = self.heap[rightIdx]
                self.heap[rightIdx] = self.heap[idx]
                self.heap[idx] = tmp
                idx = rightIdx
            else:
                return
                    
    def insert(self, nodeID, key):
        self.heap.append(Node(nodeID, key))
        self.bubbleUp(len(self.heap) - 1)
        
    def pop(self):
        output = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.bubbleDown(0)
        return output
        
    def updateKey(self, nodeID, key):
        for i in range(len(self.heap)):
            if self.heap[i].nodeID == nodeID:
                self.heap[i].key = key
                self.bubbleUp(i)
                return
            
    def printHeap(self):
        print("Heap:")
        for node in self.heap:
            print("ID:", node.nodeID, "- Key:", node.key)