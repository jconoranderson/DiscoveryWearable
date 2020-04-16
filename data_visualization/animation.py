# %%

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("../data/test_sensor_eda.csv","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)
    time.sleep(1)
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()

# %%
