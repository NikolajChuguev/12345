x=1000
y=1000
x1=x/2
y1=y/2
speed=5

def setup() :
    size(x,y)
    fill(0)

def keyPressed():
    global x1,y1
    if key == 'w':
        y1 = y1-speed
    if key == 's':
        y1 = y1+speed
    if key == 'a':
        x1 = x1-speed
    if key == 'd':
        x1 = x1+speed
def keyReleased():
    global x,y,x1,y1
    if key == ' ':
        x1 = random (0,x)
        y1 = random (0,y)
        background(255)
        ellipse(x1,y1,100,100) 
        fill(random(0,255),random(0,255),random(0,255))

def draw():
    global x1,y1
    background(255)
    ellipse(x1,y1,100,100)
