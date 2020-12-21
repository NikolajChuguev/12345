x, y = 0, 0
dim = 80.0

def setup():
   size(640, 360)
   noStroke()

def draw():
   global x, y
   background(102)

   x = x + 0.8
   if x > width + dim:
      x = -dim

   translate(x, height / 2 - dim / 2)
   fill(255)
   ellipse(-dim / 2, -dim / 2, dim, dim)
