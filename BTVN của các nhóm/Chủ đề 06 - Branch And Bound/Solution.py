class MaximumMassBasketProblem:
    def __init__(self, array, max, quantity):
        self.appleMassArray = array
        self.maximumMass = max
        self.requiredQuantity = quantity

        self.combinationNum = 0
        self.realMax = 0
        self.bestSolution = []

    def solution(self, currCom=[], currIndex=0):
        if sum(currCom) > self.maximumMass:
            return

        if len(currCom) == self.requiredQuantity:
            self.combinationNum += 1
            if sum(currCom) > self.realMax:
                self.realMax = sum(currCom)
                self.bestSolution = currCom.copy()
            return

        for index in range(currIndex, len(self.appleMassArray)):
            currCom.append(self.appleMassArray[index])
            self.solution(currCom, index + 1)
            currCom.remove(self.appleMassArray[index])

        return self.combinationNum, self.realMax, self.bestSolution


if __name__ == "__main__":
    array = list([int(mass) for mass in input().split()])
    max, quantity = [int(element) for element in input().split()]

    combinationNum, realMax, bestSolution = MaximumMassBasketProblem(array, max, quantity).solution()

    print(combinationNum)
    if combinationNum != 0:
        print(realMax)
        print(bestSolution)