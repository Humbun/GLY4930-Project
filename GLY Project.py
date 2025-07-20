# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 10:45:19 2025

@author: edend
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#create 3d shape using calc 3 eqns
#plot using 3d plots
#either simulate ball rolling or traces in a video

plt.figure(1, [8,8])
ax = plt.axes(projection = '3d')

def ellipsoid(x, y, a = 2, b = 2, c = 2, d = 1):          #optional: input d 
    
    if ((x / a) ** 2) + ((y / b) * 2) <= d ** 2:       #check that x and y < d
        N = 100
        r  = ((x ** 2) + (y ** 2)) ** 0.5
        rval = np.linspace(0, r, N)                #create arrays in polar coordinates
        thetval = np.linspace(0, 2 * np.pi, N)
        rp, tp = np.meshgrid(rval, thetval)
        
        X = rp * np.cos(tp) * a                    #converts x and y into polar coordinates
        Y = rp * np.sin(tp) * b                     #they are also 2D arrays now
        
        def posZ(meshx, meshy, a, b, c):                 #creates 2D array of z based on X and Y
            return c * ((d ** 2) - (((meshx / a) ** 2) + ((meshy / b) ** 2))) ** 0.5

        pz = posZ(X, Y, a, b, c)
        nz = - pz
        
        ax.plot_surface(X, Y, pz, cmap = 'magma')
        ax.plot_surface(X, Y, nz, cmap = 'magma_r')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.title('Ellipsoid')
        plt.tight_layout()
        plt.show()
    else: 
        d = int(input('Please input a larger integer d value:'))
        return False, d                    #if false is returned, run new d



def elliparab(x, y, a = 1, b = 1):
    N = 100
    r = ((x ** 2) + (y ** 2)) ** 0.5
    rval = np.linspace(0, r, N)                #create arrays in polar coordinates
    thetval = np.linspace(0, 2 * np.pi, N)
    rp, tp = np.meshgrid(rval, thetval)
    
    X = rp * np.cos(tp) * a                    #converts x and y into polar coordinates
    Y = rp * np.sin(tp) * b                     #they are also 2D arrays now
    
    def Z(meshx, meshy, a, b):                 #creates 2D array of z based on X and Y
        return  ((meshx / a) ** 2) + ((meshy / b) ** 2)
    
    z = Z(X, Y, a, b)
    
    ax.plot_surface(X, Y, z, cmap = 'magma')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Elliptical Parabaloid')
    plt.tight_layout()
    plt.show()

def hyperparab(x, y, a = 1, b = 1):
    N = 100
    r = ((x ** 2) + (y ** 2)) ** 0.5
    rval = np.linspace(0, r, N)                #create arrays in polar coordinates
    thetval = np.linspace(0, 2 * np.pi, N)
    rp, tp = np.meshgrid(rval, thetval)
    
    X = rp * np.cos(tp) * a                    #converts x and y into polar coordinates
    Y = rp * np.sin(tp) * b                     #they are also 2D arrays now
    
    def Z(meshx, meshy, a, b):                 #creates 2D array of z based on X and Y
        return  ((meshx / a) ** 2) - ((meshy / b) ** 2)
    
    z = Z(X, Y, a, b)
    
    ax.plot_surface(X, Y, z, cmap = 'magma')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Hyperbolic Parabaloid')
    plt.tight_layout()
    plt.show()

def ellipcone(x, y, a = 1, b = 1, c = 1):
    N = 100
    r = ((x ** 2) + (y ** 2)) ** 0.5
    rval = np.linspace(0, r, N)                #create arrays in polar coordinates
    thetval = np.linspace(0, 2 * np.pi, N)
    rp, tp = np.meshgrid(rval, thetval)
    
    X = rp * np.cos(tp) * a                    #converts x and y into polar coordinates
    Y = rp * np.sin(tp) * b                     #they are also 2D arrays now
    
    def posZ(meshx, meshy, a, b, c):                 #creates 2D array of z based on X and Y
        return c * (((meshx / a) ** 2) + ((meshy / b) ** 2)) ** 0.5
    
    pz = posZ(X, Y, a, b, c)
    nz = - pz
    
    ax.plot_surface(X, Y, pz, cmap = 'magma')
    ax.plot_surface(X, Y, nz, cmap = 'magma_r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Elliptical Cone')
    plt.tight_layout()
    plt.show()

def hypsheet(x, y, a = 1, b = 1, c = 1, d = 1):
    N = 100
    r = ((x ** 2) + (y ** 2)) ** 0.5
    rval = np.linspace(0, r, N)                #create arrays in polar coordinates
    thetval = np.linspace(0, 2 * np.pi, N)
    rp, tp = np.meshgrid(rval, thetval)
    
    X = rp * np.cos(tp) * a                    #converts x and y into polar coordinates
    Y = rp * np.sin(tp) * b                     #they are also 2D arrays now
    
    def posZ(meshx, meshy, a, b, c):                 #creates 2D array of z based on X and Y
        return c * ((d ** 2) + ((meshx / a) ** 2) + ((meshy / b) ** 2)) ** 0.5
    
    pz = posZ(X, Y, a, b, c)
    nz = - pz
    
    ax.plot_surface(X, Y, pz, cmap = 'magma')
    ax.plot_surface(X, Y, nz, cmap = 'magma_r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Hyperbalolid of Two Sheets')
    plt.tight_layout()
    plt.show()


ellipsoid(1, 1)


                