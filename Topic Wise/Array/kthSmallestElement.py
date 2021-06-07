import heapq


class Solution:
    # using Max Heap (O(n*logk))
    def kthSmallestMaxHeap(self, arr, k):
        '''
        arr : given array
        k : find kth smallest element and return using this function
        '''

        heap_ = []
        heapq.heapify(heap_)

        for ele in arr:
            if len(heap_) < k:
                heapq.heappush(heap_, -ele)

            else:
                if -ele > heap_[0]:
                    heapq.heappop(heap_)
                    heapq.heappush(heap_, -ele)

        return -heapq.heappop(heap_)

    # using Min Heap (O(k*logn))
    def kthSmallestMinHeap(self, arr, k):

        heapq.heapify(arr)

        for _ in range(k):
            res = heapq.heappop(arr)

        return res
