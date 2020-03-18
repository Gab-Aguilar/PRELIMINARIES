import matplotlib.pyplot as plt #command that imports the 'matlib.pyplot' to be able to plot a graph.
import numpy as np #command that imports 'numpy' to be able to set a range in the graph.

plt.title("PLOT of R-3.1 \n AGUILAR, GABRIEL LOUISE L. DATALGO Lab05 02-24-2020 \n i5 @2.40GHz,Win10") #prints the title of the graph.
plt.xlabel('log x') #prints the label of the x-axis.
plt.ylabel('log y') #prints the label of the y-axis.
plt.xscale('log')
plt.yscale('log')
a = np.arange(2,30**1) #sets the range of the value that substitutes the value to x.
b1 = 8*a #8 multiplies to a number 'x'.
b2 = 4*a*np.log(a) #logarithmic function
b3 = 2*(a**2) #exponential function
b4 = a**3 #exponential function
b5 = 2**a #exponential function

plt.plot(a,b1,label='8n') #prints the plot and its legend of the exponential function.
plt.plot(a,b2,label='4nlogn') #prints the plot and its legend of the logarithmic function.
plt.plot(a,b3,label='2n**2') #prints the plot and its legend of the exponential function.
plt.plot(a,b4,label='n**3') #prints the plot and its legend of the exponential function.
plt.plot(a,b5,label='2**n') #prints the plot and its legend of the exponential function.
plt.legend() #prints the legend of each plot.
plt.show() #prints the plot.
