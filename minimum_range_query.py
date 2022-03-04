from collections import deque
import math
class min_range_query:
    def __init__(self, arr):
        self.arr = arr
        self.interval_min = {}
        length = 1
        while length <= len(arr):
            increasing_queue = deque()
            for i in range(length):
                while increasing_queue and increasing_queue[-1] > arr[i]:
                    increasing_queue.pop()
                increasing_queue.append(arr[i])
            self.interval_min[(0, length - 1)] = increasing_queue[0]
            for i in range(1, len(arr) - length + 1):
                if increasing_queue and arr[i - 1] == increasing_queue[0]:
                    increasing_queue.popleft()
                while increasing_queue and increasing_queue[-1] > arr[i + length - 1]:
                    increasing_queue.pop()
                increasing_queue.append(arr[i + length - 1])
                self.interval_min[(i, i + length - 1)] = increasing_queue[0]
            length *= 2
    def range_min(self, left, right):
        length = right - left + 1
        len = 1 << int(math.log(length, 2))
        return min(self.interval_min[(left, left + len - 1)], self.interval_min[(right - len + 1, right)])
    def get_interval_mins(self):
        return self.interval_min

min_query = min_range_query([1,3,4,8,6,1,4,2])
print(min_query.get_interval_mins())
print(min_query.range_min(1, 6))
print(min_query.range_min(2, 7))
print(min_query.range_min(6, 7))