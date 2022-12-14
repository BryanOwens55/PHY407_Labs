#!/usr/bin/env python
# coding: utf-8
'''

This code is for Lab 01, Question 2, Part C. The Euler-Cromer method is implemented to simulate the orbit of an asteroid in an asteroid-Sun-Jupiter
system. The simulation duration is 20 Earth years. The initial conditions for the position and velocity parameters of Jupiter have been retained 
from Part A of Question 2 of Lab 01. The output of the code is plots of x-position vs time, y-position vs time, and x-position vs y-position (phase)
of the asteroid and Jupiter. This code was written by Dharmik Patel and Bryan Owens together.

'''

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


# In[2]:


# Set variables
delta_t = 0.0001 #0.0001
G = 39.5
M_sun = 1
M_jupiter = M_sun/1000


# In[3]:


# Create parameters

t = np.arange(0,20,delta_t)

x_roid = 3.3*t 
y_roid = 0.0*t

x_jupiter = 5.2*t
y_jupiter = 0.0*t

v_x_roid = 0.0*t
v_y_roid = 3.46*t

v_x_jupiter = 0.0*t
v_y_jupiter = 2.63*t

a_x_roid = np.zeros(len(t)-1)
a_x_roid_jup = np.zeros(len(t)-1)
a_y_roid = np.zeros(len(t)-1)
a_y_roid_jup = np.zeros(len(t)-1)

a_x_jupiter = np.zeros(len(t)-1)
a_y_jupiter = np.zeros(len(t)-1) 

# Set up initial conditions

x_roid[0] = 3.3
y_roid[0] = 0.0
x_jupiter[0] = 5.2
y_jupiter[0] = 0.0
v_x_roid[0] = 0.0
v_y_roid[0] = 3.46
v_x_jupiter[0] = 0.0
v_y_jupiter[0] = 2.63



# In[4]:


# Calculate acceleration values
def acceleration(x, y, Mass):
    # Calculate radial value
    r = (x**2 + y**2)**0.5
    # Calculate acceleration values
    a_x = -1*G*Mass*x/(r**3)
    a_y = -1*G*Mass*y/(r**3)
    return a_x, a_y


# In[5]:


# Calculate velocity values
def velocity(v_x_old, v_y_old, a_x, a_y):
    v_x_new = v_x_old + a_x * delta_t
    v_y_new = v_y_old + a_y * delta_t
    return v_x_new, v_y_new


# In[6]:


# Calculate position values
def position(x_old, y_old, v_x, v_y, a_x, a_y):
    x_new = x_old + v_x*delta_t + a_x*(delta_t**2)
    y_new = y_old + v_y*delta_t + a_y*(delta_t**2)
    return x_new, y_new


# In[7]:


# Start for loop
for i in range(len(t)-1):
    
    #JUPITER PARAMETER CALCULATIONS
    
    # Calculate Jupiter acceleration values
    a_x_jupiter[i], a_y_jupiter[i] = acceleration(x_jupiter[i],y_jupiter[i], M_sun)
    
    # Calculate Jupiter velocity values                                          
    v_x_jupiter[i+1], v_y_jupiter[i+1] = velocity(v_x_jupiter[i], v_y_jupiter[i], a_x_jupiter[i], a_y_jupiter[i])
                                              
    # Calculate Jupiter position values        
    x_jupiter[i+1], y_jupiter[i+1] = position(x_jupiter[i], y_jupiter[i], v_x_jupiter[i+1], v_y_jupiter[i+1], a_x_jupiter[i], a_y_jupiter[i])                                          
    
    
    #roid PARAMETER CALCULATIONS
    
    # Calculate roid acceleration values
    a_x_roid[i], a_y_roid[i] = acceleration(x_roid[i],y_roid[i], M_sun)
    a_x_roid_jup[i], a_y_roid_jup[i] = acceleration(x_roid[i] - x_jupiter[i],y_roid[i] - y_jupiter[i], M_jupiter)
    a_x_roid[i] = a_x_roid[i] + a_x_roid_jup[i]
    a_y_roid[i] = a_y_roid[i] + a_y_roid_jup[i]
    
    # Calculate roid velocity values
    v_x_roid[i+1], v_y_roid[i+1] = velocity(v_x_roid[i], v_y_roid[i], a_x_roid[i], a_y_roid[i])
     
    # Calculate roid position values    
    x_roid[i+1], y_roid[i+1] = position(x_roid[i], y_roid[i], v_x_roid[i+1], v_y_roid[i+1], a_x_roid[i], a_y_roid[i])
    


# In[12]:


# Plot x vs y, x vs t, y vs t

plt.plot(t, x_roid)
plt.xlabel("Time (yr)")
plt.ylabel("x-position of asteroid (Au)")
plt.title("X-position of Asteroid vs. Time")
plt.savefig("xvst_asteroid.png")
plt.show()


plt.plot(t, x_jupiter)
plt.xlabel("Time (yr)")
plt.ylabel("x-position of Jupiter (Au)")
plt.title("X-position of Jupiter vs. Time")
plt.savefig("xvst_jupiter.png")
plt.show()


plt.plot(t, y_roid)
plt.xlabel("Time (yr)")
plt.ylabel("y-position of asteroid (AU)")
plt.title("Y-position of Asteroid vs. Time")
plt.savefig("yvst_asteroid.png")
plt.show()


plt.plot(t, y_jupiter)
plt.xlabel("Time (yr)")
plt.ylabel("y-position of Jupiter (AU)")
plt.title("Y-position of Jupiter vs. Time")
plt.savefig("yvst_jupiter.png")
plt.show()


plt.plot(x_roid, y_roid)
plt.xlabel("x-position of asteroid (AU)")
plt.ylabel("y-position of asteroid (AU)")
plt.title("Phase plot of Asteroid's orbit about the Sun")
plt.savefig("phase_asteroid.png")
plt.show()


plt.plot(x_jupiter, y_jupiter)
plt.xlabel("x-position of Jupiter (AU)")
plt.ylabel("y-position of Jupiter (AU)")
plt.title("Phase plot of Jupiter's orbit about the Sun")
plt.savefig("phase_jupiter.png")
plt.show()



