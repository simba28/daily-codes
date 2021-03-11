
class BubbleSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x) for x in self.array])

    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length

        if n == 1:
            return

        for i in range(n-1):
            if self.array[i] > self.array[i+1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i]

        self.bubbleSortRecursive(n-1)

    def bubbleSortIterative(self):
        n = self.length

        for i in range(n):
            swapped = False

            for j in range(n-i-1):

                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j +
                                              1] = self.array[j+1], self.array[j]
                    swapped = True

            if not swapped:
                break


array = [64, 34, 25, 12, 22, 11, 90]

sol = BubbleSort(array)
# sol.bubbleSortIterative()
sol.bubbleSortRecursive()
print(sol)
