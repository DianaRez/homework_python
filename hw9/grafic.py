import matplotlib.pyplot as plt
n = [1, 2, 3]
T = [0.3115711212158203, 0.25955986976623535, 0.23065519332885742]
# 1,2,3 подпроцесса соответственно
f = []
for i in range(3):
    f.append(T[0]/T[i])

plt.plot(n, f, '--', color = '#C71585')
plt.grid()
plt.xlabel('n')
plt.ylabel('T[1]/T[n]')
plt.show()