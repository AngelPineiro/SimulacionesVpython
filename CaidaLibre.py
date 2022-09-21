from vpython import *
import numpy as np
scene = canvas(background=color.white, autoscale=False)

run = False
def runbutton(b): # Called when user clicks the Run/Pause button
    global run
    if run: b.text = 'Run' # b references the button
    else: b.text = 'Pause'
    run = not run

r0=vector(-14,-5,0)
v0=vector(8,15,0)
a=vector(0,-9.806,0)

posicionbase=vector(0,-5,0)
tamanhobase=vector(30,0.2,10)

base = box(pos=posicionbase, size=tamanhobase, texture=textures.wood)
bola = sphere(pos=r0, radius=0.4, color=color.red, make_trail=True, emissive=True) #, trail_type="points")
bola.v=v0
bola.a=a

attach_arrow(bola, 'v', scale=0.5, color=color.blue)
attach_arrow(bola, 'a', scale=0.5, color=color.yellow)
attach_light(bola)

button(text='Run', bind=runbutton) 

graph(title='Posición de la partícula', height=200, xtitle='<i>t</i>, s', ytitle='<i>v<sub>y</sub></i>, m')
y = gcurve(color=color.red, legend=True, label="y")
x = gcurve(color=color.black, legend=True, label="x")

t=0; dt=0.005

while bola.pos.x < tamanhobase.x*0.5 and bola.pos.y > posicionbase.y-0.1:
    rate(50) # iteraciones por segundo
    if run:
        bola.v=v0+a*t
        bola.pos=r0+v0*t+0.5*a*t**2
        y.plot(t, bola.pos.y-r0.y)
        x.plot(t, bola.pos.x-r0.x)
        t=t+dt
