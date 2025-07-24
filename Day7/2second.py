import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

xVal = []
yVal = []
index = count()


def animation(i):
    df = pd.read_csv(r"data.csv")
    x = df["x_value"]
    y1 = df["total_1"]
    y2 = df["total_2"]

    plt.cla()
    
    plt.plot(x, y1, label="Channel 1")
    plt.plot(x, y2, label="Channel 2")
    plt.legend()
    plt.tight_layout()

anim = FuncAnimation(plt.gcf(), animation, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()