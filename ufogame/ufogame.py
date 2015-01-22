from graphics import *
import time
import random

#generate window
win = GraphWin("My Circle", 800, 800)
thewin = False

def gen_random_color():
	return "#%0.2X%0.2X%0.2X" % (random.randint(1, 245), random.randint(1, 245), random.randint(1, 245))

def lose():
	#big square
	r2 = Rectangle(Point(0,0), Point(800,800))
	r2.setFill('#000000')
	r2.draw(win)
	#text
	t=Text(Point(400,400),"YOU LOSE!")
	t.setTextColor('#ffffff')
	t.draw(win)

def you_win():
	#set a global variable so you dont lose after winning
	global thewin
	thewin = True
	# big square to cover screen
	r3 = Rectangle(Point(0,0), Point(800,800))
	r3.setFill('#000000')
	r3.draw(win)
	# you win text
	t2=Text(Point(400,400),"YOU WIN!")
	t2.setTextColor('#ff00ff')
	t2.draw(win)

def main():
	#initialize images / shapes
	c = Image(Point(400,400),'ufo.gif')
	c.draw(win)
	fire = Image(Point(0, 0), 'fireball.gif')
	nova = Circle(Point(400,740), 25)
	nova.setFill('#000000')
	nova.draw(win)
	nova_right = True
	r = Rectangle(Point(0, 0), Point(5, 5))
	p = Polygon(Point(40,50),Point(75,57),Point(63,80))
	p.setWidth(5)
	p.draw(win)
	p.setFill('#000000')

	#initialize bombs count. Start at -1 because it adds one every time a rectangle appears (after you get one)
	score = -1
	scorey = Text(Point(700,50), 'bombs: '+str(score))
	# if a bomb is dropping bool
	fired = False
	# if the nova has lost a life bool
	nova_hurt = False
	nova_dead = False

	#main loop (makes a new rectangle)
	while True:
		intro_text.undraw()
		intro_text2.undraw()

		pointy = c.getAnchor()
		cirx = pointy.getX()
		ciry = pointy.getY()

		scorey.undraw()
		score += 1
		scorey = Text(Point(700,50), 'bombs: '+str(score))
		scorey.draw(win)

		if score>9:
			you_win()

		#reset the rectangle when you catch one
		r.undraw()
		recx=random.randint(50,750)
		recy=random.randint(50,750)
		r = Rectangle(Point(recx, recy), Point(recx+5, recy+5))
		r.setFill('#000000')
		r.draw(win)

		#animation loop: breaks to mainloop if you catch a rectangle
		while abs(cirx-recx)>20 or abs(ciry-recy)>20:

			#check for key presses and move ufo
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
				elif key == 'space' and fired==False and score>0:
					fired = True	
					fire = Image(Point(cirx, ciry), 'fireball.gif')
					fire.draw(win)
					score = score-1
					scorey.undraw()
					scorey = Text(Point(700,50), 'bombs: '+str(score))
					scorey.draw(win)


			pointy = c.getAnchor()
			cirx = pointy.getX()
			ciry = pointy.getY()
			coloryop = gen_random_color()
			p.setFill(coloryop)

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
			if abs(poly+5-ciry)<20 and abs(polx-15-cirx)<20:
				if thewin==False:
					lose()

			
			#nova color animation
			nova_pos = nova.getCenter()
			novx=nova_pos.getX()
			novy=nova_pos.getY()
			coloryo = gen_random_color()
			coloryo2 = gen_random_color()
			nova.setFill(coloryo)
			nova.setOutline(coloryo2)
			if nova_hurt ==False:
				nova_outline_width = novx/30
				nova.setWidth(nova_outline_width)

			#fireball movement
			fire.move(0,1)
			fire_down = fire.getAnchor()
			fire_downx = fire_down.getX()
			fire_downy=fire_down.getY()

			#if the bomb leaves the screen, you can fire again
			if fire_downy>800:
				fired=False

			# ufo and nova collision detection
			# the ufo is 30 by 40 pizels, so I am adding to find the center of the ufo
			# but it needs to collide with ANY SIDE, not the center, so I made the nova "bigger" to compensate
			# kinda hacky, because the ufo image has square corners that stick out and collide, but also the nova will overlap if they collide head-on
			if abs(novy-ciry+15)<nova_outline_width+35 and abs(novx-cirx+20)<nova_outline_width+35:
				lose()

			#bomb and nova collision detection
			#the fireball is a smaller image, so less compensation on the nova size
			if abs(novy-fire_downy+2)<nova_outline_width+10 and abs(novx-fire_downx+2)<nova_outline_width+10:
				if nova_hurt == True:
					nova_dead =True
					nova.undraw()
					p.setWidth(0)
					nova.move(0,200)
				#move instead of undraw so it doesn't keep going invisibly to kill the nova on the first hit
				fire.move(0,100)
				nova_hurt = True
				nova.setWidth(0)

			# bomb/triangle collision detection
			if abs(poly+5-fire_downy+2)<15 and abs(polx-15-fire_downx+2)<15:
				fire.move(0,800)
				if nova_dead ==True:
					you_win()

			#nova back and forth movement
			if nova_right ==True:
				nova.move(2,0)
				if novx>790:
					nova_right = False
			elif nova_right==False:
				nova.move(-2,0)
				if novx< 10:
					nova_right = True
		
			time.sleep(.01)


ii=0
intro_text=Text(Point(400,320),"BOMBS AWAY!")
intro_text.setSize(35)
intro_text.draw(win)

while ii<50:
	color_intro = gen_random_color()
	intro_text.setTextColor(color_intro)
	ii +=1
	time.sleep(.07)

intro_text2=Text(Point(400,400),"Collect bombs, destroy the evil rainbow sun, then the scary triangle! Watch out!")
intro_text2.setSize(15)
intro_text2.draw(win)

while ii<100:
	color_intro = gen_random_color()
	intro_text.setTextColor(color_intro)
	ii +=1
	time.sleep(.07)




main()