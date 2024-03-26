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

  #Area of SQuare
  #Formula=? side x side  => size*size
  #Formula=? A=1/2 x b x h. => (size*size)/2
  AreaSq=size*size
  AreaTri=(size*size)/2
  fill('lime')
  textSize(25)  
  #formatted string literal -> text along with variable to display
  text(f"Area Of Square = {AreaSq} sq. units",80,300)
  text(f"Area Of Triangle = {AreaTri} sq. units",80,250)
  
 
