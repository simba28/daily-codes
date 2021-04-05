# link => https://leetcode.com/discuss/interview-question/364618/

from typing import List


def minStepsBalance(piles: List[int]) -> int:
    """
    Time : O(N logN)
    Space : O(1)
    """

    if len(piles) < 2:
        return 0

    piles = sorted(piles, reverse=True)

    steps = 0

    for i in range(1, len(piles)):

        if piles[i] != piles[i-1]:
            steps += i

    return steps


if __name__ == "__main__":
    print(minStepsBalance([50]) == 0)
    print(minStepsBalance([10, 10]) == 0)
    print(minStepsBalance([5, 2, 1]) == 3)
    print(minStepsBalance([4, 2, 1]) == 3)
    print(minStepsBalance([4, 5, 5, 4, 2]) == 6)
    print(minStepsBalance([4, 8, 16, 32]) == 6)
    print(minStepsBalance([4, 8, 8]) == 2)
    print(minStepsBalance([4, 4, 8, 8]) == 2)
    print(minStepsBalance([1, 2, 2, 3, 3, 4]) == 9)
    print(minStepsBalance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)
