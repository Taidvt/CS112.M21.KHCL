import heapq


class Graph:
    def __init__(self, v, e):
        self.numberOfVertices = v
        self.numberOfEdges = e

        self.graph = [[float('inf') for row in range(self.numberOfVertices)] for column in range(self.numberOfVertices)]

        for edge in range(self.numberOfEdges):
            vertex1, vertex2, weight = [int(number) for number in input().split()]
            self.graph[vertex1 - 1][vertex2 - 1] = self.graph[vertex2 - 1][vertex1 - 1] = weight


class dijkstraAlgorithms:
    def __init__(self, g):
        self.graph = g

    def solution(self, source, destination):
        distance = [float('inf')] * self.graph.numberOfVertices
        visited = [False] * self.graph.numberOfVertices

        heap = []
        heapq.heappush(heap, source - 1)
        distance[source - 1] = 0

        while len(heap):
            gotVertex = heapq.heappop(heap)

            if visited[gotVertex]:
                continue
            visited[gotVertex] = True

            for vertex in range(self.graph.numberOfVertices):
                if distance[vertex] > distance[gotVertex] + graph.graph[gotVertex][vertex]:
                    distance[vertex] = distance[gotVertex] + graph.graph[gotVertex][vertex]
                    heapq.heappush(heap, vertex)

        return distance[destination - 1]


if __name__ == "__main__":
    numberOfVertices, numberOfEdges, sourceVertex, destinationVertex = [int(number) for number in input().split()]
    graph = Graph(numberOfVertices, numberOfEdges)
    findMinimumWayModel = dijkstraAlgorithms(graph)
    weightOfWay = findMinimumWayModel.solution(sourceVertex, destinationVertex)
    if weightOfWay != float('inf'):
        print(weightOfWay)
    else:
        print(-1)