\# GLY4930 Project: Plotting 3D Surfaces





This project introduces plotting 3D surfaces in python using Matplotlib. The demo is intended to get the user acquainted with the basics of creating 3D plots. The demo includes 3 test surfaces utilizing a mixture of trigonometric, polynomial, and exponential functions. The surfaces will have random noise and a gaussian filter applied to create a unique plot every time. 



In addition to the 3D surface, the following code creates a 2D graph plotting the x and y coordinates at every z value generated. To utilize this code, create a folder labeled `images` in the same location as `3D Surface Plotting.py`. The line `plt.savefig('images/imshow -' + str(n).zfill(2) + '.png')` should be uncommented to save images to the user's computer.



In the future, moving the code to an Ipython Notebook (or .ipynb file) would be ideal. In this case, matplotlib.animation can be used to create an animation within the notebook without having to same images to the user's computer. 



\#Features



The surface function, `surf`, includes 3 equations:



1. 'trig': z = np.sin(X) \* np.cos(Y) + (0.2 \* np.sin(5 \* X + Y))
2. 'trig and poly': z = np.sin(X) \* np.cos(Y) + (0.2 \* X \* Y) + (0.1 \* X \*\* 2) - (0.3 \* Y \*\* 2)
3. 'poly and exp': z = np.exp(X \*\* 2 + Y) + (X \*\* 3) - (2 \* Y \*\* 5)

&nbsp;      

\# Usage



* Spyder IDE is ideal for an interactive 3d plot, however, an Ipython Notebook will work without interactivity.



\# Package Dependencies



* python=3.12
* jupyterlab
* numpy
* matplotlib (for plotting)
* scipy (for gaussian filter)
* pandas
* Ipython (required for Ipython Notebook Animation)
