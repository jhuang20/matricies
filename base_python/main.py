from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []
m2=[[1,2,3,1],[4,5,6,1]]
m1=[[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]          
m3=ident(new_matrix())
print("testing ident matrix...")
print(print_matrix(m3))
print("testing normal matrix formation [[1,2,3,1],[4,5,6,1]]... and printability(matrix m2)")
print(print_matrix(m2))
print("matrix m1")
print(print_matrix(m1))
print("tests of matrix multiplication. 1st one is multiply m2 by identity, second is m1*m2")
print(matrix_mult(m3,m2))
print(matrix_mult(m1, m2))
print("testing lines...")
p1=[300,300,0,1]
p2=[500,200,0,1]#this is the first set of points
p3=[400,400,0,1]
matrix=add_point(matrix,1,1)
matrix=add_edge(matrix,
print(matrix)
#draw_lines( matrix, screen, color )
#display(screen)
