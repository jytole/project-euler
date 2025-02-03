import csv
import dijkstraHeap

# source: https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
with open('test.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    
# data is now imported as a list
# Run dijkstra on this list
# initialize a heap to 0 values
heap = dijkstraHeap.dijkstraHeap([])
for n in range(len(data)):
    heap.insert(n,0)
heap.pop()
heap.updateKey(1,34)
heap.updateKey(2,12)
heap.printHeap()
heap.pop()
heap.printHeap()