import random as r
import turtle as t

t.speed(0)

def snow(weight, height, color):
  t.pencolor(color)
  t.penup()
  x, y = r.randrange(-weight/2,weight/2), r.randrange(-height/2,height)
  size = r.randrange(5, 50)
  t.goto(x, y)
  t.pendown()
  snow_print(size)
    
def snow_print(side):
  for _ in range(8):
    one_stick(side)
    t.left(45)

def one_stick(side):
  for i in range(3):
    t.forward(side/4)
    for i in range(2):
      t.left(45) if i%2==0 else t.right(90) 
      t.forward(side/4)
      t.backward(side/4)
    t.left(45)
  t.backward(side/4*3)
  
for i in range(int(input())):
  weight, height = 200, 200
  color = tuple(r.randrange(1, 256) for _ in range(3))
  snow(weight, height, color)
