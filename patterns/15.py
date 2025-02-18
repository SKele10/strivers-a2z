def nLetterTriangle(n: int):
    # chr(i), i => 65 to 91, A to Z
    for row in range(n, 0, -1):
        for col in range(row):
            print(chr(65+col), end=" ")
        print()
        

nLetterTriangle(3)
