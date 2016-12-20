#Pathfinder code using recursion.

def path_finder(matrix,pos,N):
    if pos == (N-1,N-1):
        return [(N-1,N-1)]
    x,y = pos
    if x+1 < N and matrix[x+1][y] == 1:
        temp = path_finder(matrix,(x+1,y),N)
        if temp != None: return [(x,y)] + temp
    elif y+1 < N and matrix[x][y+1] == 1:
        temp = path_finder(matrix,(x,y+1),N)
        if temp != None: return [(x,y)] + temp

Matrix = [[ 1 , 1 , 1, 1 , 0], [ 0 , 1 , 0, 1 , 0], [ 0 , 1 , 0, 1 , 0], [ 0 , 1 , 0, 0 , 0], [ 1 , 1 , 1, 1 , 1]]
print path_finder(Matrix,(0,0),5)