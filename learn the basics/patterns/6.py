def nNumberTriangle(n: int) -> None:
    for i in range(n, 0, -1):
        for col in range(i):
            print(col+1, end=" ")
        print('\n', end="")
    
nNumberTriangle(3)