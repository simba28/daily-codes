class MergeSortCode:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def merge(self, first, sec):

        m = len(first)
        n = len(sec)

        ans = []

        i = j = 0
        while i < m and j < n:
            if first[i] < sec[j]:
                ans.append(first[i])
                i += 1
            else:
                ans.append(sec[j])
                j += 1

        while i < m:
            ans.append(first[i])
            i += 1
        while j < n:
            ans.append(sec[j])
            j += 1

        return ans

    def mergeSort(self, arr=[]):

        if not arr:
            arr = self.arr

        if len(arr) < 2:
            return arr

        mid = len(arr)//2
        return self.merge(self.mergeSort(arr[:mid]), self.mergeSort(arr[mid:]))


sol = MergeSortCode([12, 11, 13, 5, 6, 7, 1, 87, 4])
print(sol.mergeSort())
