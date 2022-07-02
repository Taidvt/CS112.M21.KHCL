def findMinEnergyToFinal(N, h):
    minEnergy = [0] * N

    minEnergy[1] = abs(h[1] - h[0])

    for i in range(2, N):
        cost1Step = minEnergy[i - 1] + abs(h[i] - h[i - 1])
        cost2Step = minEnergy[i - 2] + abs(h[i] - h[i - 2])
        minEnergy[i] = min(cost1Step, cost2Step)

    return minEnergy[N - 1]


if __name__ == "__main__":
    numberOfStone = int(input())
    arrayOfHeight = list(int(height) for height in input().split())
    print(findMinEnergyToFinal(numberOfStone, arrayOfHeight))