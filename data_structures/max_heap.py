class MaxHeap:
    def __init__(self):
        self._heap = []
        
    def push(self, value):
        self._heap.append(value)
        child_index = len(self._heap) - 1
        parent_index = child_index // 2
        while parent_index >= 0 and self._heap[child_index] > self._heap[parent_index]:
            self._heap[child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_index]
            child_index = parent_index
            parent_index = child_index // 2
            
    def top(self):
        if not self.empty():
            return self._heap[0]
        
        return None
        
    def pop(self):
        if self.empty():
            return
        
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        
        parent_index = 0
        
        while True:
            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2
            if right_child_index < len(self._heap) and self._heap[parent_index] < max(self._heap[left_child_index], self._heap[right_child_index]):
                if self._heap[left_child_index] > self._heap[right_child_index]:
                    self._heap[left_child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[left_child_index]
                    parent_index = left_child_index
                else:
                    self._heap[right_child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[right_child_index]
                    parent_index = right_child_index
            elif left_child_index < len(self._heap) and self._heap[parent_index] < self._heap[left_child_index]:
                self._heap[left_child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[left_child_index]
                parent_index = left_child_index
            else:
                break
            
    def empty(self) -> bool:
        return len(self._heap) == 0
                

if __name__ == "__main__":
    heap = MaxHeap()
    
    for el in [6, 3, 5, 1, 0, 4, 2]:
        heap.push(el)
        
    while not heap.empty():
        print(heap.top())
        heap.pop()