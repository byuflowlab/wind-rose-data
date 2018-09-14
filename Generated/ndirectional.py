import numpy as np
from scipy.integrate import quad
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

def gaussian(x, args):
    scale = args[0]
    mean = args[1]
    std_dev = args[2]
    f = scale*(1./np.sqrt(2.*np.pi*std_dev**2))*np.exp(-(x-mean)**2/(2.*std_dev**2))

    return f

def weibull(x, args):
    shape = args[0]
    scale = args[1]
    f = np.zeros_like(x)
    for i in np.arange(0, x.size):
        if x[i] >= 0.0:
            f[i] = (shape/scale)*((x[i]/scale)**(shape-1.))*np.exp(-(x[i]/scale)**shape)

    return f

def generate_windrose(primary_directions, primary_direction_weights, primary_dir_spread, n_windrose_directions, distribution):

    directions = np.linspace(0, 360.-360./n_windrose_directions, n_windrose_directions)
    print directions
    probabilities = np.zeros(n_windrose_directions)
    dir_width = 360./n_windrose_directions

    if distribution is 'gauss':
        for d in np.arange(0, primary_directions.size):
            scale = primary_direction_weights[d]
            mean = primary_directions[d]
            std_dev = primary_dir_spread[d]
            args = [scale, 0.0, std_dev]
            directions_calc = directions - mean

            for i in np.arange(0, n_windrose_directions):
                if directions_calc[i] > 180:
                    directions_calc[i] = directions_calc[i] - 360.
                lower_limit = directions_calc[i]-dir_width/2.
                upper_limit = directions_calc[i]+dir_width/2.
                p, _ = quad(gaussian, a=lower_limit, b=upper_limit, args=args)
                probabilities[i] += p
    # elif distribution is 'weibull':
    #     for d in np.arange(0, primary_directions.size):
    #         shape = primary_direction_weights[d]
    #         scale = primary_directions[d]
    #         std_dev = primary_dir_spread[d]
    #         args = [shape, scale]
    #         for i in np.arange(0, directions.size):
    #             lower_limit = directions[i]-dir_width/2.
    #             upper_limit = directions[i]+dir_width/2.
    #             probabilities[i] += quad(weibull, a=lower_limit, b=upper_limit, args=args)
    else:
        raise ValueError("incorrect distribution spec, %s" % distribution)

    if np.sum(probabilities) != 1.0:
        probabilities -= (np.sum(probabilities)-1.0)/n_windrose_directions

    return directions, probabilities

if __name__ == "__main__":

    pd = np.array([270., 90., 20.])
    pdw = np.array([.45, 0.25, .30])
    pds = np.array([30., 30., 30.])
    ndirs = 100
    dist = 'gauss'

    x, p = generate_windrose(pd, pdw, pds, ndirs, dist)

    np.savetxt('directional_windrose.txt', np.c_[x, np.ones(ndirs)*8.0, p], header='bidirectional gaussian windrose: deg, prob, speed')
    ticks = [1./ndirs, 2./ndirs, 3./ndirs]

    plot_windrose(x, p, ticks=ticks, tick_angle=90, ticklabels=True, show=True)

