# Control Systems Toolbox
This is a tool-box GUI made using Tkinter package in Python meant for visualising and analysing control systems.

The idea behind this toolbox is based on the Control Systems toolbox in Matlab. However, Matlab not being an open source software, cannot be accessed by everyone.
This toolbox is primarily for the electrical and electronics engineers who wish to easily analyse control systems in an open source platform.

User can get time and frequency response plots and get transfer function properties by giving the coefficients of the transfer function as inputs.
Control, and Matplotlib modules are used for analysis and plotting. PIL library is used to handle images.


## Home Screen
The user can select from the three options:
 1. View Transfer Function
 2. Make Plots
 3. Transfer Function Properties

![](Images/Main.JPG)

## Plots Screen
By giving space separated coefficients of numerator and denominator of the transfer function, user can get the time and frequency response plots of the system.

![](Images/Plots.JPG)

For this sample transfer function the following plots can be obtained:

##### Step Response:

![](Images/Step.png)

##### Impulse Response:

![](Images/Impulse.png)

##### Bode Plot:

![](Images/Bode.png)

##### Nyquist Plot:

![](Images/Nyquist.png)

##### Root Locus:

![](Images/RL.png)

## Transfer Function Properties
By giving space separated coefficients of numerator and denominator of the transfer function, user can get the following for the transfer fucntion:   
 1. Minimum transfer function
 2. DC Gain
 3. Poles
 4. Zeros
 
 ![](Images/Properties.JPG)
 
To run this toolbox, you should have Tkinter package installed in your system. Download and run the main.py file to start using.
Icons used from www.flaticon.com 

