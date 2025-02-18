def nNumberTriangle(n: int) -> None:
    start = 1
    for row in range(n):
        for col in range(row+1):
            print(start, end=" ")
            start += 1
        print()
nNumberTriangle(3)
