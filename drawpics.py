from turtle import*

#Task 1
def drawLine(a,l):
    left(a)
    forward(l)
#drawLine(45,10)

#Task 2   
def drawStar():

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)

    drawLine(45,10)
    drawLine(180,10)
    drawLine(180,0)
       
    drawLine(0,10)
       
#drawStar()

#Task 3
def drawRectangle(x,y):
    for n in range(2):
        drawLine(90,x)
        drawLine(90,y)
       
#drawRectangle(50,90)

#Task 4
def drawArch():
    drawLine(90,30)
#inner circle
    circle(10,180)

    drawLine(0,30)
    drawLine(270,10)
    drawLine(270,35)
    circle(-20,180)
    drawLine(0,35)
    drawLine(270,10)
    drawLine(180,0)


#drawArch()

#Task 5
def DrawPicture():
#moutain 1
    penup()
    setpos(0,170)
    pendown()
    drawLine(26.5650512,178.8854382)
    drawLine(270,134.16407865)
    penup()
#moutain 2
    setpos(180,210)
    pendown()
    drawLine(90,178.8854382)
    drawLine(270,134.16407865)
    penup()
#moutain 3
    setpos(390,190)
    pendown()
    drawLine(90,178.8854382)
    drawLine(270,134.16407865)
    drawLine(63.4349488,0)	
    penup()
#star 1
    setpos(50,330)
    pendown()
    drawStar()
    penup()
#star 2
    setpos(90,290)
    pendown()
    drawStar()
    penup()
#star 3
    setpos(130,330)
    pendown()
    drawStar()
    penup()
#star 4
    setpos(210,360)
    pendown()
    drawStar()
    penup()
#star 5
    setpos(250,290)
    pendown()
    drawStar()
    penup()
#star 6
    setpos(380,340)
    pendown()
    drawStar()
    penup()
#star 7
    setpos(440,280)
    pendown()
    drawStar()
    penup()
#star 8
    setpos(520,330)
    pendown()
    drawStar()
    penup()
#castle 1
    setpos(80,20)
    pendown()
    drawLine(0,50)
    drawLine(90,100)
    drawLine(296.5650512,22.360679775)
    drawLine(63.4349488,20)
    for c in range(4):
        drawLine(90,10)
        drawLine(90,10)
        drawLine(270,10)
        drawLine(270,10)
    
    drawLine(90,10)
    drawLine(90,20)
    drawLine(63.4349488,22.360679775)
    drawLine(296.5650512,100)
    drawLine(90,0)
    penup()
    
#window 1
    setpos(100,60)
    pendown()
    drawRectangle(10,10)
    penup()
    drawLine(0,20)
    pendown()
    drawRectangle(10,10)
    penup()
#window2
    setpos(100,80)
    pendown()
    drawRectangle(10,10)
    penup()
    drawLine(0,20)
    pendown()
    drawRectangle(10,10)
    penup()
#window3
    setpos(100,100)
    pendown()
    drawRectangle(10,10)
    penup()
    drawLine(0,20)
    pendown()
    drawRectangle(10,10)
    penup()

#casle 2
    setpos(330,20)
    pendown()
    drawLine(0,50)
    drawLine(90,100)
    drawLine(296.5650512,22.360679775)
    drawLine(63.4349488,20)
    for c in range(4):
        drawLine(90,10)
        drawLine(90,10)
        drawLine(270,10)
        drawLine(270,10)
    
    drawLine(90,10)
    drawLine(90,20)
    drawLine(63.4349488,22.360679775)
    drawLine(296.5650512,100)
    drawLine(90,0)
    penup()

#window 4
    setpos(350,60)
    pendown()
    drawRectangle(10,10)
    penup()
    drawLine(0,20)
    pendown()
    drawRectangle(10,10)
    penup()
#window 5
    setpos(350,80)
    pendown()
    drawRectangle(10,10)
    penup()
    drawLine(0,20)
    pendown()
    drawRectangle(10,10)
    penup()
#window 6
    setpos(350,100)
    pendown()
    drawRectangle(10,10)
    penup()
    drawLine(0,20)
    pendown()
    drawRectangle(10,10)
    penup()
    
#arch 2
    setpos(430,50)
    pendown()
    drawArch()
#arch 3
    penup()
    setpos(480,70)
    pendown()
    drawArch()
#arch 4
    penup()
    setpos(530,90)
    pendown()
    drawArch()
#arch 1
    penup()
    setpos(240,20)
    pendown()
    drawArch()
    penup()


#trees upper 1
    penup()
    setpos(510,40)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)

#trees upper 2
    penup()
    setpos(540,40)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
#trees upper 3
    penup()
    setpos(570,40)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
#trees upper 4
    penup()
    setpos(600,40)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
#trees bottom 5
    penup()
    setpos(470,0)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
#trees bottom 6
    penup()
    setpos(500,0)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
    #trees bottom 7
    penup()
    setpos(530,0)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
    #trees bottom 8
    penup()
    setpos(560,0)
    pendown()
    drawLine(90,20)
    for t in range(4):
        drawLine(135,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(270,14.1421356237)
        drawLine(180,14.1421356237)
        drawLine(315,5)
    
    drawLine(135,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(270,14.1421356237)
    drawLine(180,14.1421356237)
    drawLine(225,0)
    penup()

        

#wall 1
    penup()
    setpos(140,50)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
    
#Wall 2
    penup()
    setpos(135,45)
    pendown()
    drawRectangle(5,5)
    for k in range(7):
        drawLine(0,10)
        drawRectangle(5,10)
    drawLine(0,5)
    drawRectangle(5,5)
#Wall 3,1
    penup()
    setpos(140,40)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)

#Wall 4,2
    penup()
    setpos(135,35)
    pendown()
    drawRectangle(5,5)
    for k in range(7):
        drawLine(0,10)
        drawRectangle(5,10)
    drawLine(0,5)
    drawRectangle(5,5)

#Wall 5,1
    penup()
    setpos(140,30)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
#Wall 6,2
    penup()
    setpos(135,25)
    pendown()
    drawRectangle(5,5)
    for k in range(7):
        drawLine(0,10)
        drawRectangle(5,10)
    drawLine(0,5)
    drawRectangle(5,5)
#Wall 7,1
    penup()
    setpos(140,20)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
    penup()


#wall 2.1
    penup()
    setpos(260,50)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
    
    
#Wall 2.2
    penup()
    setpos(255,45)
    pendown()
    drawRectangle(5,5)
    for k in range(7):
        drawLine(0,10)
        drawRectangle(5,10)
    drawLine(0,5)
    drawRectangle(5,5)


#wall 2.3
    penup()
    setpos(260,40)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
    

    
#Wall 2.4
    penup()
    setpos(255,35)
    pendown()
    drawRectangle(5,5)
    for k in range(7):
        drawLine(0,10)
        drawRectangle(5,10)
    drawLine(0,5)
    drawRectangle(5,5)


#wall 2.5
    penup()
    setpos(260,30)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
    



    
#Wall 2.6
    penup()
    setpos(255,25)
    pendown()
    drawRectangle(5,5)
    for k in range(7):
        drawLine(0,10)
        drawRectangle(5,10)
    drawLine(0,5)
    drawRectangle(5,5)





#wall 2.7
    penup()
    setpos(260,20)
    pendown()
    for i in range(7):
        drawRectangle(5,10)
        drawLine(0,10)

    drawRectangle(5,10)
    
    penup()
        
    
DrawPicture()

done()
speed(10)
