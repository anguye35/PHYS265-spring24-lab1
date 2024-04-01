#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:26:27 2022
Modified on Fri Mar 11 15:26:27 2022
@author: Your name

Description
------------
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from lab1a_utilities import calculate_force
from lab1a_utilities import calculate_potential

# In ipython console for the docstring, type:
# import lab1a_utilities as util
# util.calculate_potential?

# Type for game window: import lab1a_Nguyen as game

# Create the source charges (2D numpy array with 3 columns and rows = # of charges)

a = ([-1,30,20],
     [1,-20,10],
     [1,-95,-40])
q = np.array(a)

# Set the default initial conditions for v0, angle, and y0
v0, angle, y0 = 50.0, 30.0, 30.0    
# Keep x0 fixed at -100
x0 = -100.

def clear():
    
    # NO NEED TO EDIT THIS FUNCTION

    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    ax.cla()
    ax.axis('square')
    ax.set_xlim(-200,200)
    ax.set_ylim(-200,200)
    ax.set_title('Electrostatic Projectile Game',fontsize=16)
    ax.set_xlabel('x position (meters)',fontsize=16)
    ax.set_ylabel('y position (meters)',fontsize=16)
    ax.grid(visible=True)
    fig.tight_layout()    
    fig.show()
    return
fig = plt.figure('Game Window')
ax = fig.add_subplot()
clear()


############################################################

def play():

    # NO NEED TO EDIT THIS FUNCTION

    global v0, angle, y0
    
    print("Starting x location is -100")
    v0 = float(input("Enter the initial speed between zero and 100.\n"))
    assert(v0 >= 0 and v0 <= 100), "Initial velocity should > 0 and < 100"
    angle = float(input("Enter the initial angle in degrees.\n"))
    assert(angle >= -180.00 and angle <= 180.00), \
        "Angle should be between -180 and +180"
    y0 = float(input("Enter the initial y position.\n"))
    assert(y0 >= -200 and y0 <= 200), "y0 should be between -200 and +200"
    
    plot_trajectory()
    
    return
 


############################################################

def reveal_potential():

    fig = plt.figure('Game Window')
    # for a 3D wireframe or surface plot, comment out this line:
    ax = fig.axes[0]
    # game.reveal_potential()
    # fig.clf()
    # ax = fig.add_subplot(projection='3d')

    xx = np.arange(-200,200,5)
    yy = np.arange(-200,200,5)
    X, Y = np.meshgrid(xx,yy)
    
    Z = np.zeros(len(xx)*len(yy)).reshape(len(xx),len(yy))
    for i in range(len(xx)):
        for j in range(len(yy)):
            Z[i,j] = calculate_potential(X[i,j],Y[i,j],q)

    ax.contour(X,Y,Z,levels=np.linspace(-10000,10000,41))

    return

############################################################

def reveal_forcefield():
    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    
    # your code goes here


    return

############################################################


############################################################

def plot_trajectory():

    # game.plot_trajectory()
    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    
    nt = 41
    t0 = 0.0
    t1 = 20
    t = np.linspace(t0,t1,nt)
    
    def derivatives(t,s):
        Fx, Fy = calculate_force(v0,angle,q)
        D = np.zeros(3)
        D[0] = s[3]
        D[1] = s[4]
        D[2],D[3] = Fx, Fy
        return D
    
    sol = solve_ivp(derivatives,(t0,t1),[x0,v0],t_eval=t)
    pos = sol.y[0]
    
    ax.plot(t,pos,marker='o')
    fig.show()
    
    return

############################################################

def solve_it():
    
    sol1 = 2
    sol2 = 1
    sol3 = 1
    sol4 = 3
    
    quad1 = False
    while quad1 == 0:
        ans1 = int(input('Does quadrant 1 have (1) positive charge; (2) negative charge; (3) neither; or (4) both?\n'))     
        if ans1 == sol1:
            print("That's correct!")
            quad1 = True
        else:
            print("Sorry, try again")
            quad1 = False
    
    quad2 = False
    while quad2 == 0:
        ans2 = int(input('How about quadrant 2?\n'))
        if ans2 == sol2:
            print("That's correct!")
            quad2 = True
        else:
            print("Sorry, try again")
            quad2 = False
    
    quad3 = False
    while quad3 == 0:
        ans3 = int(input('Quadrant 3?\n'))
        if ans3 == sol3:
            print("That's correct!")
            quad3 = True
        else:
            print("Sorry, try again")
            quad3 = False
        
    quad4 = False
    while quad4 == 0:
        ans4 = int(input('Quadrant 4?\n'))
        if ans4 == sol4:
            print("That's correct!")
            quad4 = True
        else:
            print("Sorry, try again")
            quad4 = False
    
    print("Congradulations!")

    return









