import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('bmh')

# Stat 
xVal = []
yVal = []
index = count()

def animate(i):
    xVal.append(next(index))
    yVal.append(random.randint(0, 5))
    
    plt.cla()
    plt.plot(xVal, yVal)
    
anim = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

