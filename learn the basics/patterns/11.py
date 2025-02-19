def nBinaryTriangle(n: int) -> None:
    for row in range(n):
        for col in range(row+1):
            print((row+col+1) % 2, end=" ")
        print()
        
nBinaryTriangle(3)
