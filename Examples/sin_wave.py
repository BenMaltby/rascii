import rascii
import time
import math

window = rascii.new_window(100, 60)  # (width, height)
window.bg_color = ' '
rascii.border_color = '*'
window.border = False
window.setup()

def main():

	points = []
	y = 0
	r = 15
	t = 0
	ytran = 30

	while True:

		window.clear()  # erase screen data
		rascii.clear_console()  # clear actual console

		y = round(r * math.sin(t)) + ytran
		points.insert(0, y)

		for i in range(0, len(points)-1, 1 if len(points) > 1 else 1):
			if len(points) > 1:
				rascii.line(window, i+9, points[i], (i+1)+9, points[i+1])
			else:
				rascii.point(window, i+9, points[i])

		if len(points) > 89:
			del points[len(points) - 1]

		t += 0.2

		window.draw()  # draw contents of screen data
		time.sleep(0.01)

if __name__ == '__main__':
	main()
