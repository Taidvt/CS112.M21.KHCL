class SubsetSumProblem:
    def __init__(self, size, sum, array):
        self.sizeOfArray = size
        self.givenSum = sum
        self.array = array
        self.ans = 0

    def combinationSum(self, currSum=0, currIndex=0):
        if (currSum > self.givenSum):
            return

        if (currSum == self.givenSum):
            self.ans += 1
            return

        for index in range(currIndex, self.sizeOfArray):
            currSum += self.array[index]
            self.combinationSum(currSum, index + 1)
            currSum -= self.array[index]

        return self.ans


if __name__ == "__main__":
    size, sum = [int(element) for element in input().split()]
    array = list([int(element) for element in input().split()])
    solution = SubsetSumProblem(size, sum, array)
    print(solution.combinationSum())
