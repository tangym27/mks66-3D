from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()



# from the gallery
parse_file( 'script', edges, transform, screen, color )

# given test file from source code
parse_file( 'script2', edges, transform, screen, color )

# gallery submission
parse_file( 'script3', edges, transform, screen, color )
