import turtle as t
import colorsys as cs
t.bgcolor('black')
t.width(8)
t.speed(0)
t.tracer(30)
h = 0

for i in range(600):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(c)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(i/4, 60)
    t.rt(20)
    t.up()
    t.goto(0,0)
    t.down()
    t.circle(i/4, 30)
    t.rt(55)
    t.fd(i/6)
    t.end_fill()
    
t.done()
