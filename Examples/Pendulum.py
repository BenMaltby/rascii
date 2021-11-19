# Code from Daniel Shiffman

import rascii
import time
import math

window = rascii.new_window(100, 60)  # (width, height)
window.bg_color = ' '
rascii.border_color = '*'
window.border = False
window.setup()

def main():
	angle = math.pi/4
	angleV = 0
	angleA = 0
	bx, by = 0, 0
	length = 40
	gravity = 0.05
	xtranslate = int(window.width/2)
	ytranslate = int(window.height/12)

	while True:

		window.clear()  # erase screen data
		rascii.clear_console()

		force = gravity * math.sin(angle)
		angleA = (-1 * force) / length
		angleV += angleA
		angle += angleV

		bx = round(length * math.sin(angle) + xtranslate)
		by = round(length * math.cos(angle) + ytranslate)

		rascii.color = '*'
		rascii.line(window, xtranslate, ytranslate, bx, by)

		rascii.color = '.'
		rascii.fill, rascii.fill_color = True, window.bg_color
		rascii.circle(window, bx, by, 6)

		window.draw()  # draw contents of screen data
		time.sleep(0.01)

if __name__ == '__main__':
	main()
