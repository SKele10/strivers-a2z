def triangle(n:int) ->None:
    for row in range(n):
        for col in range(row+1):
            print(f'{col+1} ', end="")
        print('\n', end="")
        
triangle(5)