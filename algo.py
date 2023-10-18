import random as rm
position_x=int(input("Position x="))
position_y=int(input("Position y="))
rx=int(input("Horizontal Amplitude="))
ry=int(input("Vertical Amplitude="))
intes=int(input("Intensity="))

px1=position_x-rx
px2=position_x+rx
if px1<0:
    px1=0

py1=position_y-ry
py2=position_y+ry
if py1<0:
    py1=0

intensity=4*rx*ry*intes/100
h=int(intensity)

for i in range(h):
    x=rm.randint(px1,px2)
    y=rm.randint(py1,py2)
    print("x=",x)
    print("y=",y)