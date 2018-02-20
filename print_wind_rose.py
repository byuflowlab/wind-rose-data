import numpy as np
from utilities import plot_windrose

if __name__ == "__main__":

    wind_data = np.loadtxt("./Nantucket/nantucket_windrose_ave_speeds.txt")
    wd = wind_data[:, 0]
    ws = wind_data[:, 1]
    wf = wind_data[:, 2]
    ticks = np.array([2, 3, 4, 5])
    unit = '%'
    # print wf
    # # sum
    indexes = np.where(wind_data[:, 1] > 0.1)
    windDirections = wind_data[indexes[0], 0]
    windFrequencies = wind_data[indexes[0], 2]
    wind_dirs_temp = np.zeros([12])
    wind_freq_temp = np.zeros([12])
    for i in range(0, 12):
        wind_dirs_temp[i] = np.average(windDirections[i * 3:(i + 1) * 3])
        wind_freq_temp[i] = np.sum(windFrequencies[i * 3:(i + 1) * 3])
    wd = wind_dirs_temp
    wf = wind_freq_temp
    size = np.size(windDirections)
    # print wf

    # np.savetxt('nantucket_wind_rose_for_LES.txt', np.c_[wd, np.ones_like(wd)*8.0, wf], header='direction (deg), speed (m/s), frequency')

    # average
    # indexes = np.where(wind_data[:, 1] > 0.1)
    # windDirections = wind_data[indexes[0], 0]
    # windFrequencies = wind_data[indexes[0], 2]
    # wind_dirs_temp = np.zeros([12])
    # wind_freq_temp = np.zeros([12])
    # for i in range(0, 12):
    #     wind_dirs_temp[i] = np.average(windDirections[i * 3:(i + 1) * 3])
    #     wind_freq_temp[i] = np.average(windFrequencies[i * 3:(i + 1) * 3])
    # wd = wind_dirs_temp
    # wf = wind_freq_temp
    # size = np.size(windDirections)

    # select
    # indexes = np.argpartition(ws, -10)[-10:]
    # dummy = np.zeros(wd.size)
    # dummy[indexes] = 1.0
    # print dummy
    # wf = dummy*wf
    # print wf

    print wd, wf
    plot_windrose(wd[:], wf[:]*100, ticks, unit=unit, save=True)


