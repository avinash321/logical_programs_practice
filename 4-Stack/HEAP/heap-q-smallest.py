import heapq
arr = [7, 10, 4, 3, 20, 15]
k = 3

heap = []

for n in arr:
    heapq.heappush(heap, n)
    if len(heap) > k:
        heapq.heappop(heap)

print(heap)