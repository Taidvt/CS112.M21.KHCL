def findNumberOfWaysToClimbTheTop(N):
    if N == 1:
        return 1

    if N == 2:
        return 2

    numberOfWays = [0] * N

    numberOfWays[0] = 1
    numberOfWays[1] = 2

    for i in range(2, N):
        numberOfWays[i] = numberOfWays[i - 1] + numberOfWays[i - 2]

    return numberOfWays[N - 1]


if __name__ == "__main__":
    numberOfStairs = int(input())
    print(findNumberOfWaysToClimbTheTop(numberOfStairs))