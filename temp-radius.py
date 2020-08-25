import numpy as np
import matplotlib.pyplot as plt
#Lennard Jones Plot
r = np.linspace(0, 75, num=16)
print(r)

epsilon = -10.24
sigma = 78.06
###### Create figure ######
# figsize = dimensions of the figure
# dpi = resolution
# constrained_layout = True tries to make sure everything plotted is inside the display window
plt.figure(figsize=[3,5],dpi=300,constrained_layout=True)
### Figure text sizes ######
fontsize=7
## tick_params sets the tick sizes i.e. the numbers on the axes
## axis sets the axis for which you are setting the fontsize
plt.tick_params(axis='y',labelsize=fontsize) # would only set the fontsize for y axis
plt.tick_params(which='both',labelsize=fontsize,direction='out',length=2) # both will do it for both major and minor ticks
temp = []

for value in r:
    t = np.log(value)
    T = (epsilon * t) + sigma
    # print(t)
    temp.append(T)


print(temp)


#Elj= 4*epsilon*((sigma/r)**12 - (sigma/r)**6)

plt.plot(r, temp, '-H',color='red', markeredgecolor='black',markeredgewidth=0.5,label='Data set 1')

#For different values of sigma and epsilon------------------
epsilon = -10.10
sigma = 77.47

temp = []

for value in r:
    t = np.log(value)
    T = (epsilon * t) + sigma
    # print(t)
    temp.append(T)


print(temp)
# alpha to set transparency (between 0 and 1)
# lw : linewidth

plt.plot(r, temp, '-X', color='blue',markeredgecolor='black',markeredgewidth=0.5,lw=1,alpha=0.6, label='Data Set 2')
plt.title("Distance v Temperature",fontsize=fontsize)
plt.xlim(0.0, 90.0)
plt.ylim(0, 100)
# starting with r allows you to use Latex for math symbols by placing them inside $ $

plt.ylabel(r'Temperature$(^\circ C)$', color='red', fontsize=fontsize)
plt.xlabel(r'$r_{center}$(mm)', color='red', fontsize=fontsize)
# frame on false removes the box around the legend
plt.legend(loc='best',fontsize=7,frameon=False)
plt.grid(True)
plt.show()


