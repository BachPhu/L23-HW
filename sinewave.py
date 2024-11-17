#Source: https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/

#Importing required library
import numpy as np
import matplotlib.pyplot as plt

# Creating x axis with range and y axis with Sine
# Function for Plotting Sine Graph
frequency = 3;
x = np.arange(0, 5*np.pi, .1)
y = np.sin(frequency*x)

# Plotting Sine Graph
plt.plot(x, y, color='green')
plt.show()

