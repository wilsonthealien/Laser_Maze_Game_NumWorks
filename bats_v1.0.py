# "Bats" by Wilson
from math import *
from kandinsky import *
from ion import *
from random import *
from time import *
pause=True
loop=True
chased=False
chased_timer=-300
rand_col=(randint(0,255),randint(0,255),randint(0,255))
def left():
  global px,py,pw,ph,bg
  px-=1
  fill_rect(px+pw,py,1,ph,bg)
  if px<1:
    px=1
def right():
  global px,py,pw,ph,bg
  px+=1
  fill_rect(px-1,py,1,ph,bg)
  if px+pw>321:
    px=321-pw
  if px<1:
    px=1
pscore=0  
px=20
py=200
pw=8
ph=10
pc=(0,0,120)
penergy=30
plife=3
bats_total=0
bats=randint(3,10)
batx=randint(300,350)
baty=randint(80,150)
batw=10
bath=3
rect_color="black"
bg=(231,210,240)#(randint(0,225),randint(0,225),randint(0,225))
fill_rect(0,0,322,222,bg)
draw_string("RGB:"+str(bg),0,25,"black",bg)
fill_rect(0,0,322,18,"cyan")
fill_rect(0,19,322,3,"black")
while loop:
  penergy-=0.0001
  baty+=randint(-2,2)
  batx-=1
  chased_timer+=1
  draw_string("Life:"+str(int(plife)),0,0,"black","cyan")
  draw_string("Energy:"+str(int(penergy)),80,0,"blue","cyan")
  draw_string("Score:"+str(int(pscore)),210,0,"black","cyan")
  draw_string("Bats:"+str(bats),220,24)    
  fill_rect(px,py,pw,ph,pc)
  fill_rect(0,211,322,20,rand_col)
  fill_rect(batx+1,baty+1,2,2,"red")
  fill_rect(batx,baty,batw,bath,rect_color)
  fill_rect(batx+batw,baty-batw,batw,batw*2,bg)
 
  if chased_timer>randint(200,300):
    chased=choice([0,1,1])
    chased_timer=0
  if chased:
    if baty<=py:
      baty+=1
    if baty>=py:
      baty-=1
  if keydown(KEY_LEFT):
    left()
  if keydown(KEY_RIGHT):
    right()
  if batx < - batw-5 :
    fill_rect(0,0,322,18,"cyan")
    batx=randint(300,400)
    baty=randint(100,210)
   
  if baty<22:
    baty=22
#player gets hit
  if batx >= px and batx<=px+pw and baty+bath >= py and baty <= py+ph:
    penergy-=4
    fill_rect(px+choice([-4,-2]),py+choice([-4,-2]),randint(2,3),randint(1,3),pc)
    fill_rect(px,py,pw,ph,"red")  
    fill_rect(0,0,322,18,"cyan")
  if penergy<1:
    penergy=30
    plife-=1
  if plife<1:
    loop=False
   
  if keydown(KEY_OK):
    penergy-=0.01
    fill_rect(145,0,35,18,"cyan")
    fill_rect(px+6,py+4,14,2,choice(["white","black"]))
    sleep(0.005)
    pass
    fill_rect(px+6,py+4,14,2,bg)
    if batx>=px+pw+12 and batx<=px+pw+12 and baty+bath>=py and baty<=py+ph :
      fill_rect(batx,baty,batw,bath,bg)
      batx=randint(260,330)
      baty=randint(100,210)
      chased=0
      penergy+=4
      pscore+=randint(25,100)
      bats-=1
      bats_total+=1
      draw_string("      ",230,24,bg,bg)    
 
  if bats<1:
    bats=randint(3,10)
    bg=(randint(0,255),randint(0,255),randint(0,255))
    fill_rect(0,20,322,222,bg)
    draw_string("RGB:"+str(bg),0,25,choice(["black","white"]),bg)
    rand_col=(randint(0,200),randint(0,200),randint(0,200))
    fill_rect(0,211,322,20,rand_col)
    batw=randint(5,12)
    bath=randint(2,6)      
     
  if penergy>30:
    penergy=2
    plife+=1
     
     
  if keydown(KEY_BACKSPACE) or pause:
    draw_string("(PAUSED)",110,50,"black",bg)
    draw_string("Key [Backspace] = Pause/Resume",10,70,"black",bg)
    draw_string("key [OK] = Attack",100,90,"black",bg)
    while keydown(KEY_BACKSPACE):
      pass
      pause=1
    while not keydown(KEY_BACKSPACE):
      pass
      pause=0
    while keydown(KEY_BACKSPACE):
      draw_string("        ",110,50,bg,bg)
      draw_string("                              ",10,70,bg,bg)
      draw_string("                  ",100,90,bg,bg)
 
      pass
      pause=0
for i in range(150):
    for j in range(110):
      i=randint(0,321)
      j=randint(0,222)
      fill_rect(i,j,randint(3,9),randint(3,9),(100,0,0))
draw_string("GAME OVER",100,70,(255,)*3,(100,0,0))      
draw_string("SCORE:"+str(pscore),100,100,"green",(100,0,0))
draw_string("BATS KILLED: "+str(bats_total),100,130,"cyan",(100,0,0))
fill_rect(0,0,322,40,(269,)*3)
fill_rect(0,182,322,40,(269,)*3)
