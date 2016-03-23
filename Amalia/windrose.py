from matplotlib import pyplot as plt
import numpy as np

def importMonth(file):
    import xlrd

    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)

    directions = np.array([cell.value for cell in sheet.col(39)[2:]])
    speeds = np.array([cell.value for cell in sheet.col(44)[2:]])

    # throw out the error (-99999) values
    indices = [i for i in range(len(speeds)) if directions[i]>-99999 and speeds[i]>-99999]
    directions = directions[indices]
    speeds = speeds[indices]

    return directions, speeds

import fnmatch
import os

files = [file for file in os.listdir('.') if fnmatch.fnmatch(file, 'OWEZ_M_181_200*')]
directions = np.array([])
speeds = np.array([])
for fileI, file in enumerate(files):
    print fileI+1
    directionsM, speedsM = importMonth(file)
    directions = np.append(directions, directionsM)
    speeds = np.append(speeds, speedsM)

directionRes = 22.5

speedEdges = [0,4,7,11,16,22,100]#np.arange(0.0,np.ceil(speeds.max())+1.0,1.0)
speedEdges = np.arange(0.0,np.ceil(speeds.max())+1.0,1.0)
directions[directions>(360-directionRes/2)] = directions[directions>(360-directionRes/2)] - 360.
directionEdges = np.arange(0,360+directionRes,directionRes) - directionRes/2

binsizes,_,_ = np.histogram2d(speeds, directions, np.array([speedEdges, directionEdges]))

p = binsizes/np.sum(binsizes)

directionCenters = (directionEdges[0:-1]+directionEdges[1:])/2

fig = plt.figure(figsize=(8,8)) 
#plt.title('Wind Speed/Direction Frequency.', fontsize=13) 
ax = fig.add_axes(([0.15,0.15,0.725,0.725]), polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2.0)
colors = ['b','c', 'g', 'y', 'r', 'k']

bars = list()

b = plt.bar(np.radians(directionCenters), p[0], width=np.radians(directionRes), align='center', color=colors[0], bottom=0, linewidth=0)
bars.append(b)
for i in range(1,len(speedEdges)-1):
    b = plt.bar(np.radians(directionCenters), p[i,:], width=np.radians(directionRes), align='center', color=colors[i], bottom=np.sum(p[:i], 0), linewidth=0) 
    bars.append(b)
    plt.legend(bars, ('0-4 m/s', '4-7 m/s', '7-11 m/s', '11-16 m/s', '16-22 m/s', '22+ m/s'), loc='lower right')
plt.show() 