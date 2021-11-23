import rascii
import time
import math

window = rascii.new_window(200, 120)  # (width, height)
window.bg_color = ' '
rascii.border_color = '*'
window.border = False
window.setup()

def main():

	t = 0
	wave = []
	rascii.color = '*'

	amount = 10  # change for a different wave
	
	while True:

		window.clear()  # erase screen data
		rascii.translateVector = [int(window.width*0.25), int(window.height*0.5)]

		x = 0
		y = 0

		for i in range(amount):
			prevx = round(x)
			prevy = round(y)

			n = i*2+1
			radius = (int(window.width*0.125) * (4 / (n*math.pi)))
			x += round(radius * math.cos(n*t))
			y += round(radius * math.sin(n*t))

			rascii.fill = False
			rascii.circle(window, prevx, prevy, round(radius))

			rascii.line(window, prevx, prevy, x, y)

		wave.insert(0, y)

		rascii.translateVector = [int(window.width*(1/2)), int(window.height*0.5)]

		data = []
		for j in range(len(wave)-1):
			data.append(j)
			data.append(wave[j])

		rascii.shape(window, data, False)

		t += 0.1

		if len(wave) > int(window.width/2):
			del wave[len(wave) - 1]

		window.draw()  # draw contents of screen data
		time.sleep(0.01)  # Time should be adjusted to fit program

if __name__ == '__main__':
	main()

# Must run in command prompt
# No Ending yet so use "ctrl + c" to stop
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

Translate:
	rascii.translateVector = [xtranslation, ytranslation]

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

Shape:
	rascii.shape(window, point_data, connected=True/False)
"""
