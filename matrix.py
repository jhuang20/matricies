"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    ret=''
    
    for x in range(len(matrix[0])):
        it=0
        while it<len(matrix):
            ret+=str(matrix[it][x])+' '
            it+=1
        ret+='\n'
    return ret
        
        
        

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        matrix[i][i]=1
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    mtemp=new_matrix(len(m1),len(m2))
    for cols in range(len(mtemp[0])):#goes through matrix col by col
        for item in range(len(mtemp)):
            to_add=0
            for second in range(len(mtemp[0])):
                to_add+=m2[item][second]*m1[second][cols]
            mtemp[item][cols]=to_add 

    m2=mtemp
    
    
    return print_matrix(m2)




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
