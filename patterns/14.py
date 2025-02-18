def nLetterTriangle(n: int) -> None:
    # chr(i), i => 65 to 91, A to Z
    for row in range(n):
        for col in range(row+1):
            print(chr(65+col), end=" ")
        print()
        
nLetterTriangle(3)