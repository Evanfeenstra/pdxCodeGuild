from graphics import *
import time
import random

win = GraphWin("My Circle", 800, 800)

def gen_random_color():
	return "#%0.2X%0.2X%0.2X" % (random.randint(1, 245), random.randint(1, 245), random.randint(1, 245))

def main():
	c = Circle(Point(400,400),10)
	coloryo = gen_random_color()
	c.setOutline(coloryo)
	c.setFill(coloryo)
	c.draw(win)
	size = 1

	r = Rectangle(Point(0, 0), Point(5, 5))
	r.draw(win)

	while True:
		coloryo = gen_random_color()
		c.setOutline(coloryo)
		c.setFill(coloryo)
		c.setWidth(size)
		size += 1
		pointy = c.getCenter()
		cirx = pointy.getX()
		ciry = pointy.getY()
		radius = c.getRadius()

		#if cirx-recx<20:
		r.undraw()
		recx=random.randint(50,750)
		recy=random.randint(50,750)
		r = Rectangle(Point(recx, recy), Point(recx+5, recy+5))
		r.setFill('#000000')
		r.draw(win)

		while abs(cirx-recx)>radius or abs(ciry-recy)>radius:
			key = win.checkKey()
			if key:
				if key == 'Up':
					c.move(0,-5)
				elif key == 'Down':
					c.move(0,5)
				elif key == 'Left':
					c.move(-5,0)
				elif key == 'Right':
					c.move(5,0)	
				elif key == 'space':
					coloryo = gen_random_color()
					c.setOutline(coloryo)
					c.setFill(coloryo)

			pointy = c.getCenter()
			cirx = pointy.getX()
			ciry = pointy.getY()

			time.sleep(.001)
		#c.draw(win)



main()