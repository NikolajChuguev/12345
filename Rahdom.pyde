x1=0
y1=0
x=1000
y=1000

def setup() :
    size(x,y)
    fill(0,0,0)
def keyReleased():
    global x,y,x1,y1
    if key == ' ':
        x1 = random (0,x)
        y1 = random (0,y)
        background(0) 
        ellipse(x1,y1,100,100)
        fill(random(0,255),random(0,255),random(0,255))

def draw():
    q=0
