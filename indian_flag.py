import turtle as t

t.speed(4)

t.begin_fill()  #white box
t.color('white')
t.forward(200)
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()

t.begin_fill() #green box
t.color('green')
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()


t.up() # turtle for home point
t.goto(200, 40)
t.down()

t.begin_fill() #orange box
t.color('orange')
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()


t.up() #middle blue circle
t.home()
t.forward(100)
t.down()
t.begin_fill()
t.color('blue')
t.circle(20)

t.left(90)
t.forward(40)

t.backward(20)
t.left(90)
t.forward(20)
t.backward(40)
t.forward(20)
t.left(45)
t.forward(20)
t.backward(40)

t.forward(20)
t.right(90)
t.forward(20)
t.backward(40)

t.shape("circle")
t.up()
t.forward(20)
t.down()

t.hideturtle()

