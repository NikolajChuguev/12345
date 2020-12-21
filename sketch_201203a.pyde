colorr=0
colorg=0
colorb=0
def setup():
    size (1000,1000)
    background(0)
def draw(): 
    global colorr,colorg,colorb
    if mouseX>450 and mouseY>450 and mouseY<550 and mouseX<550:
        colorr=255
        colorg=0
        colorb=0
    else :
        colorr=255
        colorg=255
        colorb=255
    fill(colorr,colorg,colorb)
    ellipse(500,500,100,100)
