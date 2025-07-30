# GLY4930 Project: Plotting 3D Surfaces





This project introduces plotting 3D surfaces in Python using Matplotlib. The demo is intended to get the user acquainted with the basics of creating 3D plots and includes 3 test surfaces utilizing a mixture of trigonometric, polynomial, and exponential functions. The surfaces will have random noise and a gaussian filter applied to create a unique plot every time. 



In addition to the 3D surface, the following code creates a 2D graph plotting the x and y coordinates at every z value generated. The points are grouped and the plots saved, which can be "played" to demonstrate the change in surface height.


<p float="left">
  <img src="\example_images\trig_surface_example.png" width="230" />
  <img src="\example_images\imshow -00.png" width="230" />
  <img src="\example_images\imshow -11.png" width="230" /> 
  <img src="\example_images\imshow -29.png" width="230" />
</p>





In the future, moving the code to an Ipython Notebook (or .ipynb file) would be ideal. In this case, matplotlib.animation can be used to create an animation within the notebook without having to same images to the user's computer. 


&nbsp;   

# Features



The surface function, `surf`, includes 3 equations:



1. 'trig': z = np.sin(X) \* np.cos(Y) + (0.2 \* np.sin(5 \* X + Y))
2. 'trig and poly': z = np.sin(X) \* np.cos(Y) + (0.2 \* X \* Y) + (0.1 \* X \*\* 2) - (0.3 \* Y \*\* 2)
3. 'poly and exp': z = np.exp(X \*\* 2 + Y) + (X \*\* 3) - (2 \* Y \*\* 5)


The user will be prompted to input the name of one of these 3 equations. 

&nbsp;      

# Installation and Running

Spyder IDE is ideal for an interactive 3d plot, however, an Ipython Notebook will work without interactivity. To use in Spyder, download `3d Surface Plotting.py`. Alternatively, `3d Surface JL.ipynb` should be used for Jupyter Labs/Notebook.


Both files include code that saves images to the user's computer as plots are created. To utilize this code, create a folder labeled `images` in the same location as the `.py` or `.ipynb` files. The line `plt.savefig('images/imshow -' + str(n).zfill(2) + '.png')` should be uncommented to save images. This folder will have to be emptied before running the code again since `plt.savefig()` does not write over images.



If the user is using **conda** instead


## Package Dependencies

To run in Jupyter Labs, download the `surfaces.yml` file or create a `.yml` with the following dependencies:

* python=3.12
* jupyterlab
* numpy
* matplotlib
* scipy
* pandas
* Ipython
  * required for Ipython Notebook Animation
 
All packages are available in Jupyter Notebook or Spyder.
