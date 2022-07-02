import sys


class MaximumProdOfSubSetProblem:
    def __init__(self, quantity, array):
        self.sizeOfArray = quantity
        self.array = array

    def solution(self):
        if self.sizeOfArray == 1:
            return self.array[0]

        maxNev = -sys.maxsize
        countZero = countNev = 0
        maxProd = 1

        for element in self.array:
            if element == 0:
                countZero += 1
                continue

            if element < 0:
                countNev += 1
                maxNev = max(maxNev, element)

            maxProd *= element

        if countZero == self.sizeOfArray:
            return 0

        if countZero == self.sizeOfArray - 1 and countNev == 1:
            return 0

        if maxProd < 0:
            maxProd //= maxNev

        return maxProd


if __name__ == "__main__":
    quantity = int(input())
    array = list([int(element) for element in input().split()])

    print(MaximumProdOfSubSetProblem(quantity, array).solution())