import sys


class MaximumSumOfSubArrayProblem:
    def __init__(self, quantity, array):
        self.sizeOfArray = quantity
        self.array = array

    def maxSumSubOfArray(self, left, right, step=1):
        maxSum = -sys.maxsize
        total = 0

        for index in range(left, right, step):
            total += self.array[index]
            if total > maxSum:
                maxSum = total

        return maxSum

    def solution(self, left, right):
        if left == right:
            return self.array[left]

        middle = (left + right) // 2

        leftMaxSum = self.maxSumSubOfArray(middle, left - 1, -1)
        rightMaxSum = self.maxSumSubOfArray(middle + 1, right + 1)

        return max(leftMaxSum + rightMaxSum,
                   self.solution(left, middle),
                   self.solution(middle + 1, right))


if __name__ == "__main__":
    quantity = int(input())
    array = list([int(element) for element in input().split()])

    maximumSumOfSubArray = MaximumSumOfSubArrayProblem(quantity, array).solution(0, quantity - 1)

    print(maximumSumOfSubArray)