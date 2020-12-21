width = height = 1000
ny = 6
nx = 6
l = 100
var = 0
def setup(): 
    size(width, height)
    stroke(0,128,0)
    noFill()
    frameRate(4)    
def draw():
    global var 
    background(192,192,192)
    for i in range(ny):
           for k in range(nx):
               x = ((k+1)*width/nx)-((width/nx)/2)
               y = ((i+1)*height/ny)-((height/ny)/2)
               if var == 0 :
                   line(x, y-(l/2), x, y+(l/2))
               if var == 1 :
                   rect(x-l/2, y-l/2, l, l)
                   fill(255,255,0) 
               if var == 2 :
                   ellipse(x, y, l, l)
                   fill(255,204,0)    
    if frameCount %1 == 0 :
       var = (var+1)%3 
        
