#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *
import numpy as np
scene = canvas(background=color.white, autoscale=False)
import sympy as sp
sp.init_printing() # for LaTeX formatted output
import sympy.physics.vector as spv
import IPython.display as disp

run = False
def runbutton(b): # Called when user clicks the Run/Pause button
    global run
    if run: b.text = 'Run' # b references the button
    else: b.text = 'Pause'
    run = not run

t = sp.symbols('t')
R= spv.ReferenceFrame('R')
amplitud=5
r_t=amplitud*(-sp.cos(2*t)*R.x+sp.sin(2*t)*R.y) # disp.display(r_t)
v_t=r_t.diff(t,R) # disp.display(v_t)
a_t=v_t.diff(t,R) # disp.display(a_t)
#spv.dot(r_t, v_t)

tempo=0
posx=spv.dot(r_t, R.x).evalf(subs={t: tempo})
posy=spv.dot(r_t, R.y).evalf(subs={t: tempo})
velx=spv.dot(v_t, R.x).evalf(subs={t: tempo})
vely=spv.dot(v_t, R.y).evalf(subs={t: tempo})
acx=spv.dot(a_t, R.x).evalf(subs={t: tempo})
acy=spv.dot(a_t, R.y).evalf(subs={t: tempo})

r0=vector(posx, posy, 0)
v0=vector(velx,vely,0)
a0=vector(acx,acy,0)

bola = sphere(pos=r0, radius=0.4, color=color.red, make_trail=True, emissive=True)
bola.v=v0
bola.a=a0
attach_arrow(bola, 'v', scale=0.25, color=color.blue)
attach_arrow(bola, 'a', scale=0.25, color=color.yellow)
attach_light(bola)
button(text='Run', bind=runbutton)

tempo=0

posiciones=graph(title='Posición de la partícula', height=200, xtitle='<i>t</i>', ytitle='<i>x,y</i>')
velocidades=graph(title='Velocidad de la partícula', height=200, xtitle='<i>t</i>', ytitle='<i>v<sub>x</sub></i>, <i>v<sub>y</sub></i>')
trayectoria=graph(title='Trayectoria de la partícula', width=300, height=300, xtitle='<i>x</i>', ytitle='<i>y</i>')
hodografa=graph(title='Hodógrafa de la partícula', width=300, height=300, xtitle='<i>v<sub>x</sub></i>', ytitle='<i>v<sub>y</sub></i>')

x = gcurve(color=color.black, legend=True, label="x", graph=posiciones)
y = gcurve(color=color.red, legend=True, label="y", graph=posiciones)
vx = gcurve(color=color.black, legend=True, label="x", graph=velocidades)
vy = gcurve(color=color.red, legend=True, label="y", graph=velocidades)

trj=gcurve(color=color.black, graph=trayectoria)
hod=gcurve(color=color.black, graph=hodografa)

tempo=0
while (tempo <8):
    rate(10)
    if run:
        tempo=tempo+0.1
        posx=spv.dot(r_t, R.x).evalf(subs={t: tempo})
        posy=spv.dot(r_t, R.y).evalf(subs={t: tempo})
        velx=spv.dot(v_t, R.x).evalf(subs={t: tempo})
        vely=spv.dot(v_t, R.y).evalf(subs={t: tempo})
        acx=spv.dot(a_t, R.x).evalf(subs={t: tempo})
        acy=spv.dot(a_t, R.y).evalf(subs={t: tempo})
        bola.a=vector(acx,acy,0)
        bola.v=vector(velx,vely,0)
        bola.pos=vector(posx,posy,0)
        x.plot(tempo, posx)
        y.plot(tempo, posy)
        vx.plot(tempo, velx)
        vy.plot(tempo, vely)
        trj.plot(posx,posy)
        hod.plot(velx,vely)
        tempo=tempo+0.01


# In[ ]:




