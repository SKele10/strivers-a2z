def alphaRamp(n: int) -> None:
    # chr(i), i => 65 to 91, A to Z
    for row in range(n):
        for col in range(row+1):
            print(chr(65+row), end=" ")
        print()
        
alphaRamp(3)
