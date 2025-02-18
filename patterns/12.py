def numberCrown(n: int) -> None:
    space = (n-1)*2
    for row in range(n):
        for col in range(row+1):
                print(col+1, end=" ")
        for _ in range(space):
            print(" ", end=" ")
        for col in range(row+1, 0, -1):
                print(col, end=" ")
        space -= 2
        print()
        
numberCrown(3)

