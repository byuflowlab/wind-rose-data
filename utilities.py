import numpy as np
from matplotlib import pyplot as plt
from math import radians


def plot_windrose(direction, values, ticks, minor_ticks=0, tick_angle=-32., unit='', title='', show=True, save=False,
                  file_name='figure1.pdf', plot_radius=None):
    if plot_radius == None:
        plot_radius = max(ticks)

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

    tick_labels = list()

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
    tick_labels.append('')

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