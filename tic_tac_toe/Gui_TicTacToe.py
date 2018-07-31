import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import numpy as np
from Final import *
width=500
height=500
grid_size=3
gate_circle=np.zeros((grid_size,grid_size))
gate_cross=np.zeros((grid_size, grid_size))
occupy=np.zeros((grid_size, grid_size))

def draw_line_handler(canvas):
	global width, height, grid_size, gate_circle
	square_rc=width/grid_size
    
	for i in range(1,grid_size):
		canvas.draw_line([ (width/grid_size)*i,0],[(width/grid_size)*i,height],3,'black')
		canvas.draw_line([0,(height/grid_size)*i],[width, (height/grid_size)*i],3,'black')
	for i in range(grid_size):
		for j in range(grid_size):
			if gate_circle[i,j]:
				canvas.draw_circle([(square_rc/2)+square_rc*j,(square_rc/2)+square_rc*i],square_rc/2,2,'black' )
				occupy[i,j]=1

	for i in range(grid_size):
		for j in range(grid_size):
			if gate_cross[i,j]:
				canvas.draw_line([j*square_rc, i*square_rc], [(j+1)*square_rc, square_rc+i*square_rc],3, 'black' )
				canvas.draw_line([j*square_rc+square_rc, i*square_rc], [j*square_rc,square_rc*i+square_rc], 3,'black')
				occupy[i,j]=1

def mouse_handler(position):
	global gate_circle,next_move

	square_rc=width/grid_size
	# col_floor_1=np.floor(position[0]/square_rc)
	# row_floor_1=np.floor(position[1]/square_rc)
	row_floor=np.floor(position[0]/square_rc).astype(int)
	col_floor=np.floor(position[1]/square_rc).astype(int)
	if not occupy[col_floor, row_floor] :
		gate_circle[col_floor, row_floor]=1


		# gate_cross[col_floor , row_floor]=1

	next_move=(col_floor, row_floor)
	a.move(next_move, 'o')
	x_move=a.best_move('x',num_iter=2500)
	gate_cross[x_move]=1


# 	print(row_floor, col_floor)
def button_handler():
	global gate_circle, grid_size,gate_cross, occupy
	gate_circle=np.zeros((grid_size, grid_size))
	gate_cross=np.zeros((grid_size,grid_size))
	occupy=np.zeros((grid_size, grid_size))


a=TicTacToe(size=grid_size)

frame=simplegui.create_frame('alpha go',500,500,100)
frame.set_canvas_background('white')
frame.set_draw_handler(draw_line_handler)
botton1=frame.add_button('Reset', button_handler)
frame.set_mouseclick_handler(mouse_handler)
frame.start()


