# "laser_escape" Game for NumWorks
# Version 1.0
# By: Wilson
from math import *
from kandinsky import *
from kandinsky import fill_rect as F
from kandinsky import draw_string as STR
from ion import *
from ion import keydown as KEY
from ion import KEY_LEFT as LEFT
from ion import KEY_RIGHT as RIGHT
from ion import KEY_UP as UP
from ion import KEY_DOWN as DOWN
from random import *
from random import randint as RINT
from time import *
F(0,0,322,222,(0,)*3)
F(0,160,322,4,"gray")
F(0,0,322,4,"gray")
while not KEY(KEY_OK):
    STR("KEYs [Arrow] = 8 Directions",6,30,"red","black")
    STR("KEY [OK] = Slow Motion",6,55,"green","black")
    STR("KEY [Backspace] = Pause/UnPause",6,80,"gray","black")
    STR("KEY [Toolbox] = Rotate",6,105,"white","black")
    STR("( Press OK to Start )",50,180,"cyan","black")
F(0,0,322,35,"white")
end=False
bg=choice([(127,255,212),
(176,224,230),(135,206,250),
(255,192,203),(250,235,215),
(135,206,235),(128,0,0),
(255,127,80),(255,215,0),
(144,238,144),(175,238,238)
])
world=1
score=0
plife=5
px=4
py=200
pw=6
ph=3
ptravel=0
#leave this
rect_x=300
rect_y=0
rect_size=0
laser_w=10
clock=0
clock2=9
set_pixel(px,py,"blue")
set_pixel(rect_x,rect_y,"red")
p=(px,py,pw,ph,"blue")
def restart():
  global px,py,pw,ph,bg,plife
  plife-=1
  F(px,py,pw,ph,bg)
  px=3
  py=200
 
  while not KEY(KEY_OK):
    STR("Press [ok]",100,15)
  STR("          ",100,15,"white","white")
 
#generate new_world  
def new_world():
  global clock,bg,world
 
  F(0,39,322,222,"black")
 
  while not KEY(KEY_OK):
    F(0,60,322,2,"cyan")
    F(0,170,322,2,"cyan")
    STR("World:"+str(world),0,0,bg,"black")
    STR("World:"+str(world),100,80,bg,"black")
    STR("Press [ok]",100,120,"white","black")
 
  bg=choice([(127,255,212),
  (176,224,230),(135,206,250),
  (255,192,203),(250,235,215),
  (245,245,220),(255,228,196),
  (245,222,179),(255,248,220),
  (255,250,205),(0,191,255),
  (135,206,235),(128,0,0),
  (255,127,80),(255,215,0),
  (189,183,107),(255,255,0),
  (144,238,144),(175,238,238)
  ])
  clock+=1
  F(0,38,322,200,bg)
  F(317,38,3,222,"blue")    
  if clock>=0 and clock<=27:
#horizontal rect
    F(RINT(20,280),RINT(38,218),RINT(20,60),20,"red")
#parallel rect
    F(RINT(20,310),RINT(35,180),20,RINT(20,65),"red")
F(0,38,322,200,bg)
F(317,38,3,222,"blue")    
while not end:
 
  set_pixel(px,py,"blue")
  STR("World:"+str(world),0,0)
  STR("life:"+str(plife),200,17)
  STR("time:"+str(int(clock2)),200,0)
  F(0,36,322,3,"red")
  F(0,219,322,3,"red")
 
  if not KEY(LEFT):
    clock2-=0.01
  clock+=1
#lasers  
  if clock>=0 and clock<=26:
#horizontal rect
    F(RINT(20,280),RINT(38,218),RINT(20,60),5,"red")
#parallel rect
    F(RINT(20,310),RINT(35,180),8,RINT(20,65),"red")
  F(px,py,pw,ph,"blue")
  F(rect_x,rect_y,rect_size,rect_size,"red")
 
  if KEY(LEFT):
    sleep(0.002)
    px-=1
    F(px+pw,py,1,ph,bg)
    plife-=0.0001
    clock2=9
    if px>1:
      ptravel+=1
  if px<1:px=1
 
  if KEY(KEY_RIGHT):
    sleep(0.002)
    px+=1
    F(px-1,py,1,ph,bg)
    plife-=0.0001
    clock2=9
    if px+pw<321:
      ptravel+=1
  if KEY(KEY_UP):
    sleep(0.002)
    py-=1
    F(px,py+ph,pw,1,bg)
    plife-=0.0001
    clock2=9
    if py>37:
      ptravel+=1
  if py<38:py=38
 
  if KEY(KEY_DOWN):
    sleep(0.002)
    py+=1
    F(px,py-1,pw,1,bg)
    plife-=0.0001
    clock2=9
    if py+ph<222:
      ptravel+=1
  if py+ph>222:
    py=222-ph
 
  # player loses energy and restarts
  if get_pixel(px,py)==get_pixel(rect_x,rect_y):
    restart()
 
  if get_pixel(px,py+ph)==get_pixel(rect_x,rect_y):
    restart()  
  if get_pixel(px+pw,py)==get_pixel(rect_x,rect_y):
    restart()
  if get_pixel(px+pw,py+ph)==get_pixel(rect_x,rect_y):
    restart()
 
  if get_pixel(px+pw,py)==get_pixel(rect_x+5,rect_y):
    restart()
 
 
   
   
   
  if KEY(KEY_OK):
    sleep(0.05)
    STR("(slow motion)",2,17)
  else:
    STR("             ",2,17)
     
   
   
 
 
  if KEY(KEY_BACKSPACE):
    STR("(PAUSED)",70,17)
    while KEY(KEY_BACKSPACE):
      pass
    while not KEY(KEY_BACKSPACE):
      pass
    while KEY(KEY_BACKSPACE):
      STR("        ",70,17,"white","white")
      pass
   
  if px+pw>320:
    plife+=0.5
    px=4
    py=200
    clock=0
    world+=1
    new_world()
    clock2=9
 
 
  if clock2<1:
    px=4
    py=200
    clock=0
    new_world()
    clock2=9
    plife-=0.2
 
  if plife<1:
    end=True
   
  if KEY(KEY_TOOLBOX):
    sleep(0.05)
    F(px,py,pw,ph,bg)
    pw=4
    ph=7
  else:
    pw=7
    ph=4
   
for i in range(150):
    for j in range(110):
      i=RINT(0,321)
      j=RINT(0,222)
      F(i,j,RINT(3,9),RINT(3,9),(140,0,0))
STR("GAME OVER",100,70,(255,)*3,(140,0,0))      
STR("Pixels Traveled:"+str(ptravel),50,120,"gray",(140,0,0))  
STR("Score:"+str(ptravel*world),100,170,"cyan",(140,0,0))
