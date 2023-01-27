
def isvalid(x_cord,y_cord,vis,matrix):
    rows  = len(matrix)
    columns = len(matrix[0])
    if(y_cord >=0 and y_cord<rows and x_cord>=0 and x_cord<columns):
        if(matrix[y_cord][x_cord]=="O"):
            return True
        else:
            return False   
    return False



####################################################################
def bfs(matrix,x_cord,y_cord,vis):
    if(vis[y_cord][x_cord]== 0 ):
         return
    vis[y_cord][x_cord] = 1
    matrix[y_cord][x_cord] = "$"
    dy_ = [0,0,-1,1]
    dx_ = [-1,1,0,0]
    for i ,j in  dx_,dy_:
        if(vis[j+y_cord][i+x_cord] and isvalid(i+x_cord,j+y_cord,matrix,vis) ):
            bfs(i+x_cord,j+y_cord,matrix,vis)




       
