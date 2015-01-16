from graphics import *
import time
import random

win = GraphWin("My Circle", 800, 800)

def gen_random_color():
	return "#%0.2X%0.2X%0.2X" % (random.randint(1, 245), random.randint(1, 245), random.randint(1, 245))

def lose():
	r2 = Rectangle(Point(0,0), Point(800,800))
	r2.setFill('#000000')
	r2.draw(win)
	t=Text(Point(400,400),"YOU LOSE!")
	t.setTextColor('#ffffff')
	t.draw(win)

def you_win():
	r3 = Rectangle(Point(0,0), Point(800,800))
	r3.setFill('#000000')
	r3.draw(win)
	t2=Text(Point(400,400),"YOU WIN!")
	t2.setTextColor('#ff00ff')
	t2.draw(win)

def main():
	c = Circle(Point(400,400),10)
	coloryo = gen_random_color()
	c.setOutline(coloryo)
	c.setFill(coloryo)
	c.draw(win)
	size = 1

	r = Rectangle(Point(0, 0), Point(5, 5))
	r.draw(win)

	p = Polygon(Point(40,50),Point(75,57),Point(63,80))
	p.draw(win)
	p.setFill('#000000')



	while True:
		coloryo = gen_random_color()
		c.setOutline(coloryo)
		c.setFill(coloryo)
		c.setWidth(size)
		size += 1
		pointy = c.getCenter()
		cirx = pointy.getX()
		ciry = pointy.getY()

		#if cirx-recx<20:
		r.undraw()
		recx=random.randint(50,750)
		recy=random.randint(50,750)
		r = Rectangle(Point(recx, recy), Point(recx+5, recy+5))
		r.setFill('#000000')
		r.draw(win)

		while abs(cirx-recx)>size+4 or abs(ciry-recy)>size+4:
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

			ppointylist = p.getPoints()
			ppointy=ppointylist[1]
			polx = ppointy.getX()
			poly = ppointy.getY()

			if polx-15<cirx:
				p.move(1,0)
			if polx-15>cirx:
				p.move(-1,0)
			if poly+5<ciry:
				p.move(0,1)
			if poly+5>ciry:
				p.move(0,-1)
			if poly+5 == ciry and polx-15 == cirx:
				lose()

			if size>2:
				you_win()

			time.sleep(.01)
		#c.draw(win)



main()