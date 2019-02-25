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
#matrix=add_point(matrix,1,1)
matrix=add_edge(matrix,1,1,0,500,500,0)
matrix=add_edge(matrix,1,500,0,500,1,0)
matrix=add_edge(matrix,250,0,0,250,500,0)
draw_lines(matrix,screen,color)
#this is the fun part: drawing 1000 lines!
for i in range(1000):
    initX=i
    initY=i
    matrix=add_edge(matrix,initX,initY,0,abs(initX-i+250),abs(i-500),0)
    draw_lines(matrix,screen,color)
    j=i*i
    k=i*j
    color=[i%255,j%255, k%255]
    matrix=[]
save_ppm(screen,'test.ppm')
print(matrix)
draw_lines( matrix, screen, color )
display(screen)
