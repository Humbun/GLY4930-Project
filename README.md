# GLY4930 Project: Plotting 3D Surfaces





This project introduces plotting 3D surfaces in **Python** using **Matplotlib**. The demo is intended to get the user acquainted with the basics of creating 3D plots and includes 3 test surfaces utilizing a mixture of trigonometric, polynomial, and exponential functions. The surfaces will have random noise and a gaussian filter applied to create a unique plot every time. 



In addition to the 3D surface, the following code creates 2D graphs plotting the x and y coordinates at every z value generated. The points are grouped and the plots saved, which can be "played" to demonstrate the coordinates with respect to the change in surface height.


<p float="left">
  <img src="\example_images\trig_surface_example.png" width="350" />
  <img src="\example_images\imshow -00.png" width="350" />
  <img src="\example_images\imshow -11.png" width="350" /> 
  <img src="\example_images\imshow -29.png" width="350" />
</p>





In the future, moving the code to an **IPython Notebook** (or .ipynb file) would be ideal. In this case, **matplotlib.animation** can be used to create an animation within the notebook without having to save images to the user's computer. 


&nbsp;   

# Features



The surface function, `surf(name)`, includes 3 equations:



1. **trig**: Uses trigonometric functions
   - z = np.sin(X) \* np.cos(Y) + (0.2 \* np.sin(5 \* X + Y))
3. **trig and poly**: Uses trigonometric functions and polynomials
   - z = np.sin(X) \* np.cos(Y) + (0.2 \* X \* Y) + (0.1 \* X \*\* 2) - (0.3 \* Y \*\* 2)
5. **poly and exp**: Uses polynomials and exponential functions
   - z = np.exp(X \*\* 2 + Y) + (X \*\* 3) - (2 \* Y \*\* 5)


The user will be prompted to input the name of one of these 3 equations. 

&nbsp;      

# Installation and Running

**Spyder IDE** is ideal for an interactive 3D plot, however, an **Ipython Notebook** will work without interactivity. To use in **Spyder**, download `3d Surface Plotting.py`. Alternatively, `3d Surface JL.ipynb` should be used for **Jupyter Labs/Notebook**.


Both files include code that saves images to the user's computer as plots are created. To utilize this code, create a folder labeled `images` in the same location as the `.py` or `.ipynb` files. The line `plt.savefig('images/imshow -' + str(n).zfill(2) + '.png')` should be uncommented to save images. This folder will have to be emptied before running the code again since `plt.savefig()` does not save over existing images.


If the user is using **conda** instead, the repository can be cloned using ***git clone https://github.com/Humbun/GLY4930-Project.git*** in the command line. After cloning, use the *command line* to create and activate the python environment, then open **Jupyter Labs** using the following lines:
* conda env create -f "file_name.yml"
* conda activate file_name
* jupyter lab


## Package Dependencies

To run in **Jupyter Labs**, create and activate an environment using the `surfaces.yml` file or create a `.yml` with the following dependencies:

* python = 3.12
* jupyterlab
* numpy
* matplotlib
* scipy
* pandas
* IPython
  * required for **IPython Notebook** Animations
 
All packages are readily available in **Jupyter Notebook** and **Spyder** and do not have to be installed. Although not ideal, dependencies can also be installed using *pip install "dependency name"*.

&nbsp;   

# Author

The author and main contributor of this repository is Eden Dalcourt.
