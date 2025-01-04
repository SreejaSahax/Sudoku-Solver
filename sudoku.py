import numpy as np
grid=[]

while True:
    row=list(input("Row: "))
    rows=[]

    for n in row:
        rows.append(int(n))
    grid.append(rows)
    print(f"Row {len(grid)} complete. ")
    if(len(grid)==9):
        break
    

def possible(row,col,num):
    for i in range(0,9):
        if grid[row][i]==num :
            return False
    for i in range(0,9):
        if grid[i][col]==num :
            return False
    y = (row // 3) * 3
    x = (col // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if grid[y+i][x+j]==num :
                return False
    
    return True


def solve():
    global grid
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col]=num
                        solve()
                        grid[row][col]=0
                return
    print(np.matrix(grid))
    input("More possible solutions")


solve()
        