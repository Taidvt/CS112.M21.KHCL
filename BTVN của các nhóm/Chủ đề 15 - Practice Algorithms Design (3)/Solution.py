class SubsetSumProblem:
    def __init__(self, size: int, list: list, total: int):
        self.sizeOfArray = size
        self.array = list
        self.givenSum = total

        self.minSum = sum(number for number in self.array if number < 0)
        self.maxSum = sum(number for number in self.array if number > 0)

        self.dp = [[0] * (self.maxSum - self.minSum + 1) for row in range(self.sizeOfArray)]

    def findAllSubsets(self, currSum: int, currIndex: int = 0):
        if currSum < self.minSum or currSum > self.maxSum:
            return 0

        if currIndex == self.sizeOfArray:
            return 1 if currSum == 0 else 0

        if self.dp[currIndex][currSum - self.minSum]:
            return self.dp[currIndex][currSum - self.minSum]

        self.dp[currIndex][currSum - self.minSum] = self.findAllSubsets(currSum, currIndex + 1) + \
                                                    self.findAllSubsets(currSum - self.array[currIndex], currIndex + 1)

        return self.dp[currIndex][currSum - self.minSum]

    def findAndPrintAnswer(self):
        answer = self.findAllSubsets(self.givenSum)
        print(answer) if answer else print(None)


if __name__ == "__main__":
    sizeOfArray = int(input())
    array = [int(number) for number in input().split()]
    givenSum = int(input())

    model = SubsetSumProblem(sizeOfArray, array, givenSum)
    model.findAndPrintAnswer()