import matplotlib.pyplot as plt
import numpy as np
from random import randint

x = np.ones(10)
y = np.ones(10)

for i in range(10):
    x[i] *= randint(1, 100)
    y[i] *= randint(1, 100)

fig, grafico = plt.subplots()
grafico.scatter(x, y, 150, "red")
grafico.plot(x, y, "green")

plt.show()