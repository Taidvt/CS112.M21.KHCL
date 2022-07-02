import math


class ClosetPairProblem:
    def calcDistance(self, point1: tuple, point2: tuple):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def findClosetPairDistanceLE3(self, size: int, points: list):
        minDistance = float('inf')

        for index1 in range(size):
            for index2 in range(index1 + 1, size):
                if self.calcDistance(points[index1], points[index2]) < minDistance:
                    minDistance = self.calcDistance(points[index1], points[index2])

        return minDistance

    def findStripClosetDistance(self, strip: list, size: int, distance: float):
        minDistance = distance

        for index1 in range(size):
            index2 = index1 + 1

            while index2 < size and strip[index2][1] - strip[index1][1] < minDistance:
                minDistance = self.calcDistance(strip[index1], strip[index2])
                index2 += 1

        return minDistance

    def findClosetPairDistance(self, size: int, points: list):
        if size <= 3:
            return self.findClosetPairDistanceLE3(size, points)

        middle = size // 2
        middlePoint = points[middle]

        leftSub = points[:middle]
        rightSub = points[middle:]

        leftDistance = self.findClosetPairDistance(middle, leftSub)
        rightDistance = self.findClosetPairDistance(size - middle, rightSub)

        currMinDistance = min(leftDistance, rightDistance)

        strip = []
        for index in range(size):
            if abs(points[index][0] - middlePoint[0]) < currMinDistance:
                strip.append(points[index])

        strip.sort(key=lambda elements: elements[1])

        return min(currMinDistance, self.findStripClosetDistance(strip, len(strip), currMinDistance))

    def solution(self, size: int, points: list):
        points.sort()
        return self.findClosetPairDistance(size, points)


if __name__ == "__main__":
    size = int(input())
    array = [tuple(map(int, input().split())) for _ in range(size)]

    minDistance = ClosetPairProblem().solution(size, array)
    print(minDistance)