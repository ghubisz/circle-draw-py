import turtle

t = turtle.Turtle()

#radius of the circle
r = 10

#loop for printing cocentric circles
for i in range(50):
    t.circle(r *i)
    t.up()
    t.sety((r*i) * (-1))
    t.down()