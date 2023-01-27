##################################################################
#vlaidator function which will check wether current pos can be captured or
#not

def isvalid(x_cord,y_cord,matrix):
    
    rows  = len(matrix)
    columns = len(matrix[0])
    if(y_cord >=0 and y_cord<rows and x_cord>=0 and x_cord<columns):
        if(matrix[y_cord][x_cord]=="O"):
            return True
        else:
            return False   
    return False



##################################################################

# Depth first search function named as capture
def capture(matrix,x_cord,y_cord,vis):
    #print(y_cord,x_cord)
   
    
    if(vis[y_cord][x_cord] == 1 ):
         return
    vis[y_cord][x_cord] = 1
    matrix[y_cord][x_cord] = "$"
    
    dy_ = [0,0,-1,1]
    dx_ = [-1,1,0,0]
    #print(vis)
    for i  in  range(0,4):
        if(isvalid(dx_[i]+x_cord,dy_[i]+y_cord,matrix)  ):
            capture(matrix,dx_[i]+x_cord,dy_[i]+y_cord,vis)
    return

##################################################################

def main(matrix,rows,columns,vis):
    
     for row in range(0,rows):
       for column in range(0,columns):
         if(row == 0 or column ==0 or row == rows-1 or column ==columns-1):
            if(matrix[row][column]=="O"):
              capture(matrix,column,row,vis)

##################################################################

# function to print the matrix
def print_matrix(matrix):
    print()
    for i in matrix:
        for j in i:
            print(j,end = " ")
        print()






# code for taking input matrix from the user

rows = int(input("Enter the number of rows :"))
columns = int(input("Enter the number of columns :"))

#vis matrix is used to keep track of wether a cell is already traversed or not
vis = [[0 for val in range(columns)] for val2 in range(rows)]

matrix = []
print("Enter the matrix row by row")
for row in range(0,rows):
    temp = input()
    x = temp.split()
    matrix.append(x)



# calling my main function 
main(matrix,rows,columns,vis)


#changing "$" to "O" and captured O to X
for i in range(0,rows):
    for j in  range(0,columns):
        if(matrix[i][j]=="$"):
            matrix[i][j] = "O"
        elif(matrix[i][j]=="O"):
          matrix[i][j] = "X"




print_matrix(matrix)



