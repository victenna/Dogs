import turtle,time
wn=turtle.Screen()
wn.setup(1200,900)
turtle.tracer(3)
wn.bgcolor('gold')
t=turtle.Turtle('turtle')
t.penup()
t.hideturtle()
B=150
s=turtle.Shape('compound')
s1=turtle.Shape('compound')
s2=turtle.Shape('compound')

t.begin_poly()

poly1=((10,-20),(30,0),(20,-20))  #хвост
poly1_=((10,-20),(0,0),(20,-20))
poly2=((40,-110),(80,-110),(90,-120),(90,-130),(50,-130),(40,-120))
poly3=((60,-110),(80,-90),(90,-90),(80,-110))
poly4=((80,-110),(90,-110),(100,-120),(100,-130),(90,-130))
poly5=((50,-40),(70,-20),(90,-10),(100,-30),(110,-10),(110,0),(120,-10),(120,-30),(130,-40),(120,-50),(90,-50),(90,-60),(70,-40))
poly6=((80,10),(90,30),(100,30),(100,20),(100,30),(120,50),(140,50),(150,60),(160,60),(170,50),(170,30),(160,10),\
      (160,0),(170,-10),(170,-20),(160,-30),(150,-30),(140,-40),\
      (130,-40),(120,-30),(120,-10),(110,0),(110,-10),(100,-30))
poly7=((140,-40),(150,-30),(160,-30),(160,-60),(150,-60))# язык
poly8=((135,0),(140,0),(140,-10),(135,-10))
poly9=((145,10),(150,10),(150,0),(145,0))
poly10=((130,-10),(130,20),(140,10),(140,30),(150,20),(150,0),(140,0),(140,-10))
poly11=((140,-10),(150,0),(160,0),(160,-10),(150,-20),(140,-20))
poly12=((80,-90),(90,-90),(110,-90),(120,-110),(120,-120),(130,-130),(160,-130),(160,-120),(150,-110),(140,-110),(120,-50),(90,-50),(90,-80))
poly13=((150,-110),(160,-110),(170,-120),(170,-130),(160,-130),(160,-120))
poly14=((130,-40),(130,-50),(150,-110),(140,-110),(120,-50))
poly15=((20,-20),(20,-50),(30,-70),(50,-40),(70,-40),(90,-60),(90,-80),(60,-110),(40,-110),(30,-100),(10,-60),(10,-20))
s.addcomponent(poly1,'gray','black')
s.addcomponent(poly2,'gray','black')
s.addcomponent(poly3,'dim gray','black')
s.addcomponent(poly4,'dim gray','black')
s.addcomponent(poly5,'gray','black')
s.addcomponent(poly6,'gray','black')
s.addcomponent(poly10,'white','black')
s.addcomponent(poly8,'black','black')
s.addcomponent(poly9,'black','black')
s.addcomponent(poly11,'black','black')
s.addcomponent(poly12,'gray','black')
s.addcomponent(poly13,'dim gray','black')
s.addcomponent(poly14,'dim gray','black')
s.addcomponent(poly15,'gray','black')



wn.addshape('dog',s)
q=turtle.Turtle(shape='dog')
q.tilt(90)
q.up()
q.shapesize(2)
q.hideturtle()
q.goto(-400,0)
q.showturtle()

s1.addcomponent(poly7,'red','black')
wn.addshape('dog1',s1)
q1=turtle.Turtle(shape='dog1')
q1.tilt(90)
q1.up()
q1.shapesize(2)
q1.hideturtle()
q1.goto(-400,0)
q1.setheading(0)

s2.addcomponent(poly1,'gold','gold')
s2.addcomponent(poly1_,'gray','black')
wn.addshape('dog2',s2)
q2=turtle.Turtle(shape='dog2')
q2.tilt(90)
q2.up()
q2.shapesize(2)
q2.hideturtle()
q2.goto(-400,0)
q2.setheading(0)



turtle.tracer(5)
while True:
    q1.showturtle()
    q2.hideturtle()
    time.sleep(0.3)
    q1.hideturtle()
    q2.showturtle()
    
    time.sleep(0.1)