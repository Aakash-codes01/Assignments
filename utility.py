from Bfs import *

def main(matrix,rows,columns,vis):
     for row in range(0,rows):
        if(row==rows-1 or row==0):
            for column in range(0,columns):
                if(matrix[row][column]=="O" and vis[row][column]==0):
                    bfs(matrix,column,row,vis)
        else:
             if(matrix[row][0]=="O" and vis[row][column]==0):
                bfs(matrix,0,row,vis)
             if(matrix[row][column-1]=="O" and vis[row][column]==0):
                bfs(matrix,column-1,row,vis)
