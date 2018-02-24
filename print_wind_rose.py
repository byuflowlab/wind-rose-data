import numpy as np
# from utilities import plot_windrose
from math import radians
from matplotlib import pylab as plt

def plot_windrose(direction, values, ticks, minor_ticks=0, tick_angle=-32., ticklabels=False, unit='', title='', show=True, save=False,
                  file_name='figure1.pdf', plot_radius=None):
    if plot_radius == None:
        plot_radius = max(ticks)

    tick_labels = np.zeros(len(ticks))
    for i in np.arange(0, len(ticks)):
        tick_labels[i] = "%.2f" % ticks[i]

    direction += 270.
    for i in range(len(direction)):
        direction[i] = radians(direction[i]) * -1.

    N = direction.size
    bottom = 0.
    # max_height = max(ws)
    # N = 36

    width = (2 * np.pi) / N

    direction -= width / 2.

    ax = plt.subplot(111, polar=True)

    minor_tick_distance = (ticks[1] - ticks[0]) / (minor_ticks + 1.)

    if minor_ticks > 0 and len(ticks) > 1:

        for major_tick_count in range(0, len(ticks)):
            tick_labels.append('%.1f %s' % (ticks[major_tick_count], unit))

            if major_tick_count < (len(ticks)):
                for minor_tick_count in range(0, minor_ticks):
                    circle_radius = ticks[major_tick_count] + (minor_tick_count + 1) * minor_tick_distance
                    circle = plt.Circle((0.0, 0.0), circle_radius, transform=ax.transData._b,
                                        facecolor=None, edgecolor='k', fill=False, alpha=0.2,
                                        linestyle=':')
                    ax.add_artist(circle)

    ticks.append(plot_radius)

    bars = ax.bar(direction, values, width=width, bottom=bottom, alpha=0.25, color='red', edgecolor=None)

    ax.set_rgrids(ticks, angle=tick_angle)
    ax.yaxis.grid(linestyle='-', alpha=0.5)

    ax.set_yticklabels(tick_labels)

    plt.title(title, y=1.07)

    ax.set_xticklabels(['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'])

    if save:
        plt.savefig(file_name, transparent=True)
    if show:
        plt.show()


if __name__ == "__main__":

    save = False

    # wind_data = np.loadtxt("./Nantucket/nantucket_windrose_ave_speeds.txt")
    wind_data = np.loadtxt("./Amalia/windrose_amalia_directionally_averaged_speeds_36dir.txt")

    dirs = wind_data[:, 0]
    spd = wind_data[:, 1]
    prob = wind_data[:, 2]

    ticks = [0.02, 0.04]
    plot_windrose(np.copy(dirs), prob, ticks=ticks, tick_angle=90, ticklabels=True, show=True)

    ticks = [6, 8, 10]
    plot_windrose(dirs, spd, ticks=ticks, tick_angle=90, ticklabels=True, show=True)

    #
    # wd = wind_data[:, 0]
    # ws = wind_data[:, 1]
    # wf = wind_data[:, 2]
    # ticks = [2, 3, 4, 5]
    # unit = '%'
    # # print wf
    # # # sum
    # indexes = np.where(wind_data[:, 1] > 0.1)
    # windDirections = wind_data[indexes[0], 0]
    # windFrequencies = wind_data[indexes[0], 2]
    # wind_dirs_temp = np.zeros([12])
    # wind_freq_temp = np.zeros([12])
    # for i in range(0, 12):
    #     wind_dirs_temp[i] = np.average(windDirections[i * 3:(i + 1) * 3])
    #     wind_freq_temp[i] = np.sum(windFrequencies[i * 3:(i + 1) * 3])
    # wd = wind_dirs_temp
    # wf = wind_freq_temp
    # size = np.size(windDirections)

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
    plot_windrose(wd[:], wf[:]*100, ticks, unit=unit, save=save)


