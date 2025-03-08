# Homogenious_ElectroStatic_Solver
I've put together this little python script to solve the equipotential surfaces around some conductors at some potential. 
The idea behind it was to then calculate the energy contained in the field and with that, then calculate the capacitance of some complex transmission line I am designing.
This script is only working for homogenous media at the moment, but I will update it at some point. 
Obviously, this uses finite differences and for solving the equipotential surfaces I solve Laplace's equation (derived from Maxwell's equations) iteratively by convolving a 3x3x3 matrix through the discretized 3D volume. 

It's a really simple and easy-to-use script. I am not uploading the whole work because it's part of some project I am currently doing, but I find the algorithm for solving Laplace's equation interesting. 
The same script could be used to solve for isothermal surfaces in a volume according to Fourier's heat conduction law.

![Potential_Lines](/Potential_lines.png?raw=true "Potential_Lines")
