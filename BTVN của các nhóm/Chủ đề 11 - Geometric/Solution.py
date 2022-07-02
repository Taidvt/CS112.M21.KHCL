class Point:
    def __init__(self, a=None, b=None):
        self.x, self.y = [int(number) for number in input().split()] if a is None and b is None else (a, b)


class Triangle:
    def __init__(self, a=None, b=None, c=None):
        self.points = [Point(), Point(), Point()] if a is None and b is None and c is None else [a, b, c]

    def calculateArea(self):
        area = 0
        for i in range(-1, 2):
            area += self.points[i].x * self.points[i + 1].y - self.points[i].y * self.points[i + 1].x
        area = abs(area) / 2

        return area


def isAPointInsideATriangle(triangle, point):
    areaOfTriangle = triangle.calculateArea()

    areaOfSubTriangleOne = Triangle(triangle.points[0], triangle.points[1], point).calculateArea()
    areaOfSubTriangleTwo = Triangle(triangle.points[1], triangle.points[2], point).calculateArea()
    areaOfSubTriangleThree = Triangle(triangle.points[2], triangle.points[0], point).calculateArea()

    return areaOfSubTriangleOne + areaOfSubTriangleTwo + areaOfSubTriangleThree == areaOfTriangle


if __name__ == "__main__":
    triangle = Triangle()
    checkPoint = Point()

    if isAPointInsideATriangle(triangle, checkPoint):
        print("Inside")
    else:
        print("Not Inside")