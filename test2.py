import numpy as np 
import matplotlib.pyplot as plt

# skapar funktionen f(x) = x^2
def f(x):
    return x**2

x = np.linspace(-1,1)
plt.plot(x, f(x)) # ritar kurvan
plt.show()