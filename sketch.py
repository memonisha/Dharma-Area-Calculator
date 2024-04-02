from p5 import *


def setup():
  createCanvas(windowWidth,windowHeight)
  #global myfont
  loadFont("Minecraft-1.ttf","myfont")
  


def draw():

  background('black')
  drawTickAxes()
  noFill()
  stroke('green')
  strokeWeight(3)
  sx=100
  sy=100
  size=mouseX-sx
  square(sx,sy,size)
  stroke('red')
  circle(sx+size/2,sy+size/2,size)
  stroke('blue')
  triangle(sx,sy,sx+size,sy,sx+size/2,sy+size)
  textSize(30)
  textFont(assets['myfont'])
  r=random(0,255)
  g=random(0,255)
  b=random(0,255)
  fill(r,g,b)
  noStroke()
  text("Dynamic Area Calculator",50,height-100)
  areas(size)
  #what is a function?
  #collection of some lines of code particularly meant to do a task
  # every function has its uniq/ue name by which we can call it anytime.
  #WOCA---> Write ONCE call ANYTIME

def areas (size):
  AreaSq=size*size
  AreaTri=(size*size)/2
  AreaCircle=round(PI * (size/2) *(size/2))
  fill('lime')
  textSize(25)  
  #formatted string literal -> text along with variable to display
  text(f"Area Of Square = {AreaSq} sq. units",80,300)
  fill('blue')
  text(f"Area Of Triangle = {AreaTri} sq. units",80,250)
  fill('red')
  text(f"Area Of Circle = {AreaCircle} sq. units",80,200)
  


#create a separate function called "Areas" what will we do inside it...just the math...and it would also print all the areas.
# in draw you just need to call the function


#Area of SQuare
#Formula for SQuare=? side x side  => size*size
#Formula for Triangle=? A=1/2 x b x h. => (size*size)/2
#Formula for Circle=? A=PI*radius*radius => PI * (size/2) *(size/2)


  
  
 
