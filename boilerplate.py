import rascii
import time

window = rascii.new_window(100, 60)  # (width, height)
window.bg_color = ' '
rascii.border_color = '*'
window.border = False
window.setup()

def main():
	while True:

		window.clear()  # erase screen data

		#code goes here...
		#{



		#}

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
