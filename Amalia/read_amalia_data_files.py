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

np.savetxt("amalia_windrose_data.txt", np.c_[directions, speeds], header="direction, speed")