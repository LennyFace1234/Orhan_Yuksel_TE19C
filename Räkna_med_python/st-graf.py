# Ritar st graf

import matplotlib.pyplot as plt

s = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
t = [1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.15, 7.96, 8.79, 9.69]

plt.plot(t, s, '*-')
plt.title("Usain Bolt - s-t graf 100m ")
plt.xlabel("Tid i sekunder")
plt.ylabel("Sträcka i meter")
plt.show()

