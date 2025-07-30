# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 22:33:44 2025

@author: edend
"""
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import scipy.ndimage as snd

#create a 3d plot of a surface with smoothed, random noise
    #function has 3 possible surfaces to plot

plt.figure(1, [8,8])
ax = plt.axes(projection = '3d')

def surf(name):                  #create a surface using some function (choose from 3)
    x = np.linspace(0, 1)
    y = np.linspace(0, 1)
    X, Y = np.meshgrid(x, y)     #meshgrid needed for 3d plot
                                    #makes 2d plane to then plot 3d
    if name == 'trig':
        z = np.sin(X) * np.cos(Y) + (0.2 * np.sin(5 * X + Y))
    elif name == 'trig and poly':
        z = np.sin(X) * np.cos(Y) + (0.2 * X * Y) + (0.1 * X ** 2) - (0.3 * Y ** 2)
    elif name == 'poly and exp':
        z = np.exp(X ** 2 + Y) + (X ** 3) - (2 * Y ** 5)
    else: 
        print('\nName not recognized. Please type\n"trig", "trig and poly", or "poly and exp"\n')
    
    r, c = np.shape(X)          #generate array of random decimals in shape of X
    randfilt = np.random.rand(r, c)
    smooth = snd.gaussian_filter(randfilt, 1.5)     #gaussain filter to smooth plot
    Z = z * smooth
    
    return X, Y, Z
    

x, y, z = surf(str(input('Please enter name of function to use: '))) 

surface = ax.plot_surface(x, y, z, cmap = 'magma')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('3D Surface')
plt.tight_layout()
plt.show() 

#sort the values of z from min to max
    #make sure there are no repeats
#search for the indices where those values show up in z
    #those same indices correspond to x, y coordinates
    #group those coordinates to plot on 2d plane
    
#create 2d plot of x and y coordinates that correspond to a certain z
    #saves images to computer that can be selected to make "video"

plt.figure(2, [8, 8])
zround = np.round(z, decimals = 2)                  #round makes easier to ==
zsort = np.unique(np.round(np.sort(z, axis = None), decimals = 2))
                                    #sort to get every z value, listed once


cmap = mp.colormaps['magma']       #get the colors used in the 3d plot so 
numcolor = zsort.shape[0]            #batches can have the same color for their 
colors = cmap(np.linspace(0, 1, numcolor))  #respective z


for n in range(zsort.shape[0]):
    
    zval = zsort[n]
    index = np.argwhere(zround == zval)     #find every index where z = some nubmer
    xcoord = []
    ycoord = []
  
    for i, j in index:  
        
        xcoord.append(x[i, j])              #each index corresponds to an x or y 
        ycoord.append(y[i, j])                  #coordinate pair

        plt.clf()
        plt.scatter(xcoord, ycoord, color = colors[n])  #plot the entire batch of
        plt.xlim(-0.1, 1.1)                                 #coordinate pairs
        plt.ylim(-0.1, 1.1)
        plt.title(f'x and y at z = {zval}')
        plt.xlabel('x')
        plt.ylabel('y')
        
    plt.savefig('images/imshow -' + str(n).zfill(2) + '.png')  #save file to computer
    
     

     

   
    
