# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 22:33:44 2025

@author: edend
"""
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import scipy.ndimage as snd

# create a 3d plot of a surface with smoothed, random noise
# automatic view 45 degrees up and azimuth of -135 degrees

plt.figure(1, [8,8])
ax = plt.axes(projection = '3d')
ax.view_init(elev = 45, azim = -135, roll = 0)


# create a surface using some function (choose from 3)
def surf(name):                  
    x = np.linspace(0, 1)
    y = np.linspace(0, 1)
    
    # meshgrid needed for 3d plot
    # makes 2D array of x values in columns
    # and 2D array of y values in rows
    X, Y = np.meshgrid(x, y)
                                    
    if name == 'trig':
        z = np.sin(X) * np.cos(Y) + (0.2 * np.sin(5 * X + Y))
    elif name == 'trig and poly':
        z = np.sin(X) * np.cos(Y) + (0.2 * X * Y) + (0.1 * X ** 2) - (0.3 * Y ** 2)
    elif name == 'poly and exp':
        z = np.exp(X ** 2 + Y) + (X ** 3) - (2 * Y ** 5)
    else: 
        print('\nName not recognized. Please type\n"trig", "trig and poly", or "poly and exp"\n')
    
    # generate array of random decimals in shape of X
    r, c = np.shape(X)          
    randfilt = np.random.rand(r, c)
    
    # apply a gaussain filter to random array and smooth plot
    smooth = snd.gaussian_filter(randfilt, 1.5)     
    Z = z * smooth
    
    return X, Y, Z
    
name = str(input('Please enter name of function to use: '))
x, y, z = surf(name) 

# plot the surface using ax rather than plt
# inputs must all be 2D arrays (x and y are taken care of with np.meshgrid)
surface = ax.plot_surface(x, y, z, cmap = 'magma')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title(f'3D Surface: {name}')
plt.savefig('images/3d plot.png')
plt.tight_layout()
plt.show() 
    
# create 2d plot of x and y coordinates that correspond to a certain z
# that saves images to computer that can be selected to make "video"

plt.figure(2, [8, 8])

# round and sort the z values so that it's easier to index them later
zround = np.round(z, decimals = 2)                 
zsort = np.unique(np.round(np.sort(z, axis = None), decimals = 2))

# get the colors used in the 3d plot so batches can have the
# same color for their respective z values
cmap = mp.colormaps['magma']        
numcolor = zsort.shape[0]            
colors = cmap(np.linspace(0, 1, numcolor))


for n in range(zsort.shape[0]):
    
    # find every index where z is some value
    zval = zsort[n]
    index = np.argwhere(zround == zval)     
    xcoord = []
    ycoord = []
  
    for i, j in index:  
        
        # each index corresponds to an x or y coordinate
        xcoord.append(x[i, j])              
        ycoord.append(y[i, j])                 

        # plot the entire batch of coordinate pairs
        plt.clf()
        plt.scatter(xcoord, ycoord, color = colors[n]) 
        plt.xlim(-0.1, 1.1)                                 
        plt.ylim(-0.1, 1.1)
        plt.title(f'x and y at z = {zval}')
        plt.xlabel('x')
        plt.ylabel('y')
        
    # save plot to computer in "images" folder
    plt.savefig('images/imshow -' + str(n).zfill(2) + '.png')  
    
     

     

   
    
