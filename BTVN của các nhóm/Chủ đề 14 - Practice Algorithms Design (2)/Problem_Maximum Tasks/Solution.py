class MaximumTasksProblem:
    def solution(self, size: int, array: list):
        sortedTasks = array.copy()

        sortedTasks.sort(key=lambda elements: elements[1])

        lastEnd = sortedTasks[0][1]
        sortedTasks.remove(sortedTasks[0])

        maximumTasks = 1
        for start, end in sortedTasks:
            if start >= lastEnd:
                lastEnd = end
                maximumTasks += 1

        return maximumTasks


if __name__ == "__main__":
    size = int(input())
    array = [tuple(map(int, input().split())) for _ in range(size)]

    maximumTasks = MaximumTasksProblem().solution(size, array)
    print(maximumTasks)