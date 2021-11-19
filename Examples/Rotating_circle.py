import rascii
import time
import math

window = rascii.new_window(100, 60)  # (width, height)
window.bg_color = ' '
rascii.border_color = '*'
window.border = False
window.setup()

def main():

	x, y   = 0, 0
	radius = 15
	theta  = 0

	while True:

		window.clear()  # erase screen data
		rascii.clear_console()  # clear actual console

		x = round(radius * math.cos(theta)) + int(window.width/2)
		y = round(radius * math.sin(theta)) + int(window.height/2)

		rascii.color = '@'
		rascii.fill, rascii.fill_color = True, window.bg_color
		rascii.circle(window, x, y, 5)

		theta += 0.1

		window.draw()  # draw contents of screen data
		time.sleep(0.01)  # not necessary

if __name__ == '__main__':
	main()

# Delete the guide if you don't need it ⬇️



###############
#    Guide    #
###############
"""
Color:
	rascii.color = '{character}'

Fill:
	rascii.fill = True/False
	rascii.fill_color = '{character}'

Point:
	rascii.point(window, x, y)

Circle:
	rascii.circle(window, x, y, radius, Transparent=False/True)

Line:
	rascii.line(window, x1, y1, x2, y2)

Rectangle:
	rascii.rect(window, x, y, width, height, Transparent=False/True)

Triangle:
	rascii.triangle(window, x1, y1, x2, y2, x3, y3, Transparen=False/True)
"""
