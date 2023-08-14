from turtle import *
from random import randint

s_widgth = 200
s_height = 200

class Sprite(Turtle):
    def __init__(self, clr, shp,x,y):
        super().__init__()
        self.color(clr)
        self.shape(shp)
        self.x = x
        self.y = y
        self.penup()
        self.goto(self.x,self.y)
        self.step = 10

    def stepUp(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def stepDn(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def stepRht(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def stepLt(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def is_collide(self,sp):
        d = self.distance(sp.xcor(),sp.ycor())
        if d < 20:
            return True
        return False

class Enemy(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('red')
        self.shape('triangle')
        self.step = 10
        self.speed(5)
        self.penup()

    def move(self,x_s,y_s,x_e,y_e):
        self.x_s = x_s
        self.y_s = y_s
        self.x_e = x_e
        self.y_e = y_e
        self.goto(self.x_s, self.y_s)
        self.setheading(self.towards(self.x_e,self.y_e))

    def make_step(self):
        self.fd(self.step)
        if self.distance(self.x_e,self.y_e) < self.step:
            self.move(self.x_e,self.y_e,self.x_s,self.y_s)

en1 = Enemy(s_widgth,-90)
en1.move(s_widgth, -90, -s_widgth, -90)

en2 = Enemy(-s_widgth,90)
en2.move(-s_widgth, 90, s_widgth, 90)

en3 = Enemy(-90,s_widgth)
en3.move(-90, s_widgth, -90, -s_widgth)

player = Sprite('red','turtle',170,160)
coin = Sprite('yellow','circle',-170,-160)
screen = player.getscreen()

screen.onkey(player.stepUp, 'Up')
screen.onkey(player.stepDn, 'Down')
screen.onkey(player.stepRht, 'Right')
screen.onkey(player.stepLt, 'Left')
screen.listen()

score = 0
while score<3:
    en1.make_step()
    en2.make_step()
    en3.make_step()
    if player.is_collide(coin):
        score += 1
        coin.goto(randint(-80,80),randint(-80,80))

    if player.is_collide(en1) or player.is_collide(en2) or player.is_collide(en3):
        coin.hideturtle()
        break

if score == 3:
    en1.hideturtle()
    en2.hideturtle()
    en3.hideturtle()

done()