from matplotlib import pyplot as plt
import numpy as np

data = np.loadtxt("amalia_windrose_data.txt")
directions = data[:, 0]
speeds = data[:, 1]
directionRes = 5.0

speedEdges = [0, 100]#np.arange(0.0,np.ceil(speeds.max())+1.0,1.0)
directions[directions>(360-directionRes/2)] = directions[directions>(360-directionRes/2)] - 360.
directionEdges = np.arange(0,360+directionRes,directionRes) - directionRes/2

# calculate probability for each direction
binsizes,_,_ = np.histogram2d(speeds, directions, np.array([speedEdges, directionEdges]))

p = binsizes/np.sum(binsizes)
print p.shape

# calculate average speed for each direction
directionCenters = (directionEdges[0:-1]+directionEdges[1:])/2
avespeeds = np.zeros_like(p[0])

for i in range(0, directionCenters.size):
    count = 0
    for j in range(0, speeds.size):
        if directionCenters[i]-directionRes/2.+directionRes < directions[j]+directionRes < directionCenters[i]+directionRes/2.+directionRes:
            avespeeds[i] += speeds[j]
            count += 1
    if avespeeds[i] > 1:
        avespeeds[i] /= count
    else:
        avespeeds[i] = 0
# save average speeds with directions and probabilities to a file     
np.savetxt("windrose_amalia_directionally_averaged_speeds.txt", np.c_[directionCenters, avespeeds, p[0]], header="direction, average_speed, probability")
        
# plot probabilities windrose
fig = plt.figure(figsize=(8,8)) 
#plt.title('Wind Speed/Direction Frequency.', fontsize=13) 
ax = fig.add_axes(([0.15,0.15,0.725,0.725]), polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2.0)
ax.set_rgrids(np.arange(0.010,0.04, 0.01), angle=145)
# colors = ['b','c', 'g', 'y', 'r', 'k']

bars = list()
plt.rcParams.update({'font.size': 20})
# plt.yticks(np.arange(0.010,0.04, 0.01))
plt.ylim([0,0.04])
b = plt.bar(np.radians(directionCenters), p[0], width=np.radians(directionRes), 
            align='center', bottom=0, linewidth=0, color='k')
bars.append(b)
for i in range(1,len(speedEdges)-1):
    b = plt.bar(np.radians(directionCenters), p[i,:], width=np.radians(directionRes), 
                align='center', bottom=np.sum(p[:i], 0), linewidth=0) 
    bars.append(b)
#     plt.legend(bars, ('0-4 m/s', '4-7 m/s', '7-11 m/s', '11-16 m/s', '16-22 m/s', '22+ m/s'), loc='lower right')
# plt.show() 

# plot average speeds windrose
fig = plt.figure(figsize=(8,8)) 
#plt.title('Wind Speed/Direction Frequency.', fontsize=13) 
ax = fig.add_axes(([0.15,0.15,0.725,0.725]), polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2.0)
ax.set_rgrids(np.arange(6,14, 2), angle=127.5)
# colors = ['b','c', 'g', 'y', 'r', 'k']

bars = list()
plt.rcParams.update({'font.size': 20})
# plt.yticks(np.arange(6,14, 2))
plt.ylim([0,12])
b = plt.bar(np.radians(directionCenters), avespeeds, width=np.radians(directionRes), 
            align='center', linewidth=0, color='k')
bars.append(b)
for i in range(1,len(speedEdges)-1):
    b = plt.bar(np.radians(directionCenters), avespeeds[:], width=np.radians(directionRes), 
                align='center', linewidth=0) 
    bars.append(b)
#     plt.legend(bars, ('0-4 m/s', '4-7 m/s', '7-11 m/s', '11-16 m/s', '16-22 m/s', '22+ m/s'), loc='lower right')

plt.show() 