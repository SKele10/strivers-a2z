def nStarTriangle(n: int) -> None:
    for row in range(n):
        for col in range(n-1, -1, -1):
            if row >= col:
                print('*', end="")
            else:
                print(' ', end="")
        print(row*'*', end="")
        print('\n', end="")


nStarTriangle(3)
