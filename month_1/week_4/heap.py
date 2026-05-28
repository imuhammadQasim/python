class MaxHeap:

    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = \
        self.heap[index2], self.heap[index1]

    def insert(self, value):

        self.heap.append(value)

        self.heapify_up()

    def heapify_up(self):

        index = len(self.heap) - 1

        while index > 0:

            parent_index = self.get_parent_index(index)

            if self.heap[index] > self.heap[parent_index]:

                self.swap(index, parent_index)

                index = parent_index

            else:
                break


heap = MaxHeap()

heap.insert(50)
heap.insert(30)
heap.insert(100)
heap.insert(70)

print(heap.heap)