# "Cubic Duel"
# Written By: Wilson
# wilsony175@gmail.com
from math import *
from ion import *
from time import *
from random import *
from kandinsky import *

from ion import keydown as KEY
from ion import KEY_LEFT as LEFT
from ion import KEY_RIGHT as RIGHT
from ion import KEY_UP as UP
from ion import KEY_DOWN as DOWN
from ion import KEY_OK as OK
from ion import KEY_BACKSPACE as BS

from kandinsky import fill_rect as FILL
from kandinsky import draw_string as STRING
from random import randint as R

time=0

def start_menu():
  global time
 
  FILL(0,0,322,222,(0,)*3)
  while not KEY(KEY_EXE):
   
    STRING("CUBIC DUEL",100,160,(255,)*3,(20,0,200))
 
    time+=1    
    if time>0 and time<400:
      STRING("""
HISTORICAL:
 Duel: A contest between two
 people in order to settle a
 point of honor...
""",10,5,"white",(0,0,140))  
       
      STRING("PRESS [EXE] KEY to start",40,200,(0,255,255),(0,)*3)
     
    if time>400 and time<600:
        STRING("                         ",40,200,(0,20,100),(0,)*3)
    if time>600:
      time=0
  if KEY(KEY_EXE):
     
      guide_menu()
def guide_menu():
  FILL(0,0,322,222,(0,)*3)
  FILL(0,20,322,5,(200,)*3)
  FILL(0,180,322,5,(200,)*3)
  while not KEY(OK):
    STRING("KEYs [Arrow] = 8 Directions",6,60,(200,)*3,(0,)*3)
    STRING("KEY [OK] = fast LEFT/RIGHT.",6,100,(200,)*3,(0,)*3)
    STRING("KEY [Backspace] = Pause/UnPause",6,140,(200,)*3,(0,)*3)
    STRING("Press [OK] KEY",80,200,(100,)*3,(0,)*3)
       
start_menu()

game=True

bg=(0,0,140)

p_attacks=False
penergy=80
pscore=0
pdir=0
px=4
py=213
ps=8
pc=(119,25,71)


echase=0
e_run=False
echase_clock=0
edir=0
eclock=0
e_energy=200
ex=R(200,300)
ey=R(60,200)
es=10
ec=(0,)*3


FILL(0,0,322,222,bg)
FILL(0,18,322,2,(100,)*3)
FILL(0,208,20,4,(0,)*3)

FILL(3,3,es,es,(0,)*3)
FILL(10,5,2,2,(255,0,0))
   
while game:

  FILL(0,208,20,4,(0,)*3)
  FILL(0,211,20,12,(38,71,107))
  FILL(px,py,ps,ps,pc)
  FILL(ex,ey,es,es,ec)
  FILL(px+2,py+2,1,1,(0,255,255))
  FILL(px+5,py+2,1,1,(0,255,255))
  pscore+=2
  eclock+=1
  echase_clock+=1
 
  if echase_clock>R(50,100):
    echase=R(0,2)
    echase_clock=0
  if echase:
    if px+ps-2<ex:
      edir=1
    if px>ex+es-2:
      edir=2
    if py+ps-2<ey:
      edir=3
    if py>ey+es-2:
      edir=4
     
  if eclock > R(50,100):
    edir=R(1,4)
    eclock=R(-50,0)

  if edir==1:
    sleep(.005)
    ex-=1
    FILL(ex+10,ey,1,es,bg)
    FILL(ex+2,ey+2,3,1,(255,0,0))
    FILL(ex,ey+6,3,2,(50,150,0))
    if echase:
      for q in range(3):
        ex-=1
        FILL(ex+es+2,ey,2,es,bg)
       
  if edir==2:
    sleep(.005)
    ex+=1
    FILL(ex-1,ey,1,es,bg)
    FILL(ex+6,ey+2,3,1,(255,0,0))
    FILL(ex+7,ey+6,3,2,(50,150,0))
    if echase:
      for q in range(3):
        ex+=1
        FILL(ex-2,ey,2,es,bg)
     
  if edir==3:
    sleep(.005)
    ey-=1
    FILL(ex,ey+es,es,1,bg)
    FILL(ex+2,ey+1,4,1,(255,0,0))
   
 
  if edir==4:
    sleep(.005)
    ey+=1
    FILL(ex,ey-1,es,1,bg)
    FILL(ex+2,ey+9,4,1,(255,0,0))

 
  if pdir==1:
    for w in range(2):
      px-=1
      FILL(px+ps,py,1,ps,bg)
    if KEY(OK):
      p_attacks=True
      for w in range(8):
        px-=1
        FILL(px+ps,py,2,ps,bg)

   
  if pdir==2:
    for w in range(2):
      px+=1
      FILL(px-1,py,1,ps,bg)
    if KEY(OK):
      p_attacks=True
      for w in range(8):
        px+=1
        FILL(px-2,py,2,ps,bg)

 
  if pdir==3:
    for w in range(2):
      py-=1
      FILL(px,py+ps,ps,1,bg)
    if KEY(OK):
      p_attacks=True
      for w in range(4):
        py-=1
        FILL(px,py+ps,ps,2,bg)
 
  if pdir==4:
    for w in range(2):
      py+=1
      FILL(px,py-1,ps,1,bg)
    if KEY(OK):
      p_attacks=True
      for w in range(4):
        py+=1
        FILL(px,py-2,ps,2,bg)
   
  #player moves diagonal
  if pdir==5:
    px-=1
    FILL(px+ps,py,1,ps,bg)
    py-=1
    FILL(px,py+ps,ps,1,bg)
  if pdir==6:
    px+=1
    FILL(px-1,py,1,ps,bg)
    py-=1
    FILL(px,py+ps,ps,1,bg)
 
  if pdir==7:
    px-=1
    FILL(px+ps,py,1,ps,bg)
    py+=1
    FILL(px,py-1,ps,1,bg)
  if pdir==8:
    px+=1
    FILL(px-1,py,1,ps,bg)
    py+=1
    FILL(px,py-1,ps,1,bg)
 
  if KEY(LEFT) or KEY(KEY_FOUR):
    pdir=1
  if KEY(RIGHT) or KEY(KEY_SIX):
    pdir=2
  if KEY(UP) or KEY(KEY_EIGHT):
    pdir=3
  if KEY(DOWN) or KEY(KEY_TWO):
    pdir=4
 
  if KEY(KEY_SEVEN):pdir=5
  if KEY(KEY_NINE):pdir=6
  if KEY(KEY_ONE):pdir=7
  if KEY(KEY_THREE):pdir=8
  if KEY(KEY_FIVE):pdir=0
 
  if KEY(LEFT) and KEY(UP):
    pdir=5
  if KEY(RIGHT) and KEY(UP):
    pdir=6
  if KEY(LEFT) and KEY(DOWN):
    pdir=7
  if KEY(RIGHT) and KEY(DOWN):
    pdir=8
   
  if px<1:
    px=1
  if px+ps>321:
    px=321-ps
  if py<20:
    py=20
  if py+ps>222:
    py=222-ps
 
  if ex<1:
    ex=1
    edir=choice([2,3,4])
  if ex+es>321:
    ex=321-es
    edir=choice([1,3,4])
  if ey<20:
    ey=20
    edir=choice([1,2,4])
  if ey+es>222:
    ey=222-es
    edir=choice([1,2,3])
       
  if KEY(BS):
      STRING("(PAUSED)",100,50,(255,)*3,bg)
      STRING("KEYs [1,3,7,9] = outsmart cube.",14,80,(255,)*3,bg)
      STRING("KEY [OK] = fast LEFT/RIGHT.",14,110,(255,)*3,bg)
      STRING("HEALTH:"+str(int(penergy)),80,140,(255,)*3,bg)
      STRING("ENEMY:"+str(int(e_energy)),80,170,(255,)*3,bg)
   
      while KEY(BS):
        pass
      while not KEY(BS):
        pass
      while KEY(BS):
        STRING("        ",100,50,bg,bg)
        STRING("                                ",10,80,bg,bg)
        STRING("                           ",14,110,"white",bg)
        STRING("                                  ",80,140,(255,)*3,bg)
        STRING("                                  ",80,170,(255,)*3,bg)
   
   
  if px<=16:
    if py>211:
      penergy+=0.001
    if py+ps >= 207 and py+ps <= 210:
      py=206-ps
      pdir=0
   
    if py <= 211 and py >= 210:
      py=212
      pdir=0
    if py+ps>=207 and py<=210 or py+ps>=207 and py+ps<=210:
      px=18
      pdir=0  
 
  if ex<=17:
    if ey+es >= 208:
      ex=17
      edir=choice([2,3,4])
      echase=R(0,1)
 
  if px+ps >= ex and px <= ex+es and py+ps >= ey and py <= ey+es:
    FILL(px,py,ps,ps,(105,0,0))
    FILL(px-choice([0,1,2,3,-1,-2,-3,]),py+choice([1,2,3]),2,2,(105,0,0))
    FILL(px,py,ps,ps,(105,0,0))
    penergy-=0.2
    FILL(px-choice([0,1,2,-8,-9,-10]),py+ps,2,2,(0,50,0))
    if p_attacks:
      p_attacks=False
      edir=choice([1,2,3,4])
      #enemy stops for a sec and
      #loses energy.
      echase=False
      e_energy-=1
      penergy+=.3
      pscore+=R(5,20)
      FILL(20,5,322,5,bg)
      FILL(ex+R(-10,20),ey+R(-10,20),R(1,2),R(1,2),(0,)*3)
    FILL(px,py,ps,ps,(105,0,0))
    penergy-=0.05
    FILL(px-choice([0,1,2,-8,-9,-10]),py+ps,2,2,(0,50,0))
   
 
    if echase:
      for q in range(3):
        ex-=1
        FILL(ex+es+2,ey,2,es,bg)
 
  STRING(str(int(penergy)),300,0)    
   
   
  if penergy<1:game=0
 
         
  if KEY(OK):
    if pdir==1:
      for w in range(322):
        FILL(px-12,py+3,R(8,14),R(1,2),(255,)*3)
    if pdir==2:
      for w in range(322):
        w=px+R(10,15)
        FILL(px+5,py+3,R(8,14),R(1,2),(255,)*3)
   
    FILL(20,5,int(e_energy),5,(255,0,0))
   


for i in range(px-20):
  for j in range(px-20):
    i=R(0,321)
    j=R(0,222)
    FILL(i,j,R(3,9),R(3,9),(50,0,0))



STRING("GAME OVER",100,70,(255,)*3,(125,40,50))      
STRING("Score: "+str(pscore),100,120,(255,)*3,(125,40,50))
FILL(0,0,322,40,(269,)*3)
FILL(0,182,322,40,(269,)*3)

