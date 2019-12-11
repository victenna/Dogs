import turtle,time
wn=turtle.Screen()
wn.setup(1200,900)
turtle.tracer(2)
wn.bgcolor('gold')
t=turtle.Turtle('turtle')
t.penup()
t.hideturtle()
B=150
s=turtle.Shape('compound')


t.begin_poly()

poly1=((0,72),(25,100),(27,103),(28,108),(20,102),(28,112),(17,110),(35,115),(27,123),(33,120),\
       (25,135),(45,120),(50,123),(50,140),(65,118),(95,78),(150,65),(157,80),(158,100),(170,73),\
       (173,67),(172,60),(177,45),(173,53),(176,40),(172,47),(175,25),(177,20),(177,5),(175,3),\
       (158,3),(160,10),(143,20),(132,23),(123,19),(115,15),(118,3),(100,1),(88,3),(90,8),\
       (87,10),(60,25),(57,36),(56,30),(53,55),(55,61),(53,71),(50,75),(42,70),(35,45),\
       (34,60),(32,35),(29,52),(28,30),(23,48),(23,33),(12,52),(16,36),(5,55))  

s.addcomponent(poly1,'gray','black')
poly2=((85,92),(91,83),(54,43),(53,57))
s.addcomponent(poly2,'red','black')

poly3=((123,19),(132,23),(143,20),(152,15),(147,3),(125,2),(127,10))
s.addcomponent(poly3,'dim gray','gray')

poly4=((60,25),(87,10),(84,4),(70,3),(56,5),(60,10))
s.addcomponent(poly4,'dim gray','gray')

poly5=((43,106),(47,106),(50,102),(47,97),(45,96),(40,96),(39,100),(40,103))
s.addcomponent(poly5,'black','gray')
poly6=((0,72),(7,70),(15,72),(5,55))
s.addcomponent(poly6,'black','gray')





wn.addshape('dog',s)
q=turtle.Turtle(shape='dog')
q.tilt(90)
q.up()
q.shapesize(3)
q.showturtle()




'''
turtle.tracer(5)
while True:
    q1.showturtle()
    q2.hideturtle()
    time.sleep(0.3)
    q1.hideturtle()
    q2.showturtle()
    
    time.sleep(0.1)
    '''