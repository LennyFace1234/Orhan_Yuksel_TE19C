import matplotlib.pyplot as plt

s = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
t = [0, 1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 7.96, 8.79, 9.69]
v = [0] # Tom lista

for i in range(1, len(s)):
    v_i = (s[i]-s[i-1])/(t[i]-t[i-1])
    v.append(v_i) # Lägger till v_i till listan
    print(i)

# plot vt-graf
plt.plot(t, v, '*-')
plt.title("Usain Bolt 100m vt-graf")
plt.xlabel("Tiden i sekunder")
plt.ylabel("Hastigheten i m/s")
plt.grid()
plt.show()