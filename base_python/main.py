from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(3,3)
m2=new_matrix(2,3)

print(print_matrix(matrix))
print(matrix_mult(matrix, m2))
#draw_lines( matrix, screen, color )
#display(screen)
