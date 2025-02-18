def nForest(n:int) ->None:
    for row in range(n):
        for col in range(row+1):
            print('* ', end="")
        print('\n', end="")
        
nForest(5)