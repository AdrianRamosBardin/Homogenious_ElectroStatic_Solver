#This script is going to solve Laplace's Equation to solve for the the electrostatic field in 3D
#The same procedure cuold be used to find the solution to the Steady-State Fourier Heat Conduction equation

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, generate_binary_structure

N = 100                               #Grid Size (100x100x100)
grid = np.zeros((N,N,N))+0.5          #Initial Potencial for the grid (0.5 V)

#Define the conductors in the grid and their potentials
grid[30:70,30:70,20] = 4
grid[30:70,30:70,80] = 0

mask_pos = grid==1
mask_neg = grid==0

yv, xv, zv = np.meshgrid(np.arange(N),np.arange(N),np.arange(N))

#We create the Matrix (Kernel) which then will convolve with our 3D Space and converge to the solution
kern = generate_binary_structure(3,1).astype(float)/6
kern[1,1,1] = 0

#We impose the potential ant the boundary of the grid to be the same as the next to it inside the grid
#This way all the equipotential lines are perpendicular to the edged of the grid, therefore the electric fild is parallel to the edges
#That implies the edges have to be an electrical insulator
def Neumann_Boundary(a):
    a[0,:,:] = a[1,:,:]; a[-1,:,:] = a[-2,:,:]
    a[:,0,:] = a[:,1,:]; a[:,-1,:] = a[:,-2,:]
    a[:,:,0] = a[:,:,1]; a[:,:,-1] = a[:,:,-2]
    return a


iters = 2000
for i in range(iters):
    #We convolve the Kernel with the grid to update the grid
    updated_grid = convolve(grid,kern, mode='constant')

    # Boundary conditions (neumann)
    updated_grid = Neumann_Boundary(updated_grid)

    # Boundary conditions (dirchlett)
    updated_grid[mask_pos] = 1
    updated_grid[mask_neg] = 0

    grid = updated_grid

slice = 50 #Slice of the 3D solution you want to plot

plt.imshow(grid[slice], cmap='hot', interpolation='nearest')
plt.imshow(np.mod(np.gradient(grid[slice])), cmap='hot', interpolation='nearest')

plt.figure(figsize=(6,5))
CS = plt.contour(np.arange(100)/100, np.arange(100)/100, grid[slice], levels=30)
plt.clabel(CS, CS.levels, inline=True, fontsize=8)
plt.xlabel('$z$')
plt.ylabel('$y$')
plt.axvline(0.2, ymin=0.3, ymax=0.7, color='r')
plt.axvline(0.8, ymin=0.3, ymax=0.7, color='b')
plt.show()
