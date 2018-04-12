import pandas as pd
from pyntcloud.pyntcloud import PyntCloud
import numpy as np

NUMPOINTS = 100

def setcolor(color_name):
    if color_name == "green":
        return np.array([0, 0, 255]).astype(np.uint8)
    elif color_name == "blue":
        return np.array([0, 255, 0]).astype(np.uint8)
    elif color_name == "red":
        return np.array([255, 0, 0]).astype(np.uint8)
    elif color_name == "white":
        return np.array([255, 255, 255]).astype(np.uint8)
    else:
        return (np.random.uniform(size=(1, 3)) * 255).astype(np.uint8)

positions = np.random.uniform(size=(NUMPOINTS, 3)) - 0.5
points = pd.DataFrame(positions, columns=['x', 'y', 'z'])

colors = np.zeros((int(positions.size / 3),3))
for i in range(0,int(positions.size / 3)):
    colors[i][:] = setcolor('whiter')

print(positions)

points[['red', 'blue', 'green']] = pd.DataFrame(colors, index=points.index)


cloud = PyntCloud(points)
cloud.to_file("room.ply")