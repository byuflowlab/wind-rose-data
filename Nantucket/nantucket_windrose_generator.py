import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

if __name__ == "__main__":

    # data from https://wrcc.dri.edu/cgi-bin/wea_windrose2.pl
    # 2 year range of data 2010-2012
    # accessed 6/26/2017

    # frequencies of with in each direction - sum ~96.1%
    frequencies = (1E-2)*np.array([2.3, 2.6, 2.8, 2.4, 2.3, 2.0, 1.5, 1.4, 1.5, 1.4, 1.5, 1.7, 1.8, 1.8, 1.9, 2.2, 2.2, 2.3,
                            2.5, 3.1, 3.5, 4.0, 4.3, 4.6, 4.2, 4.2, 3.3, 2.9, 3.3, 3.3, 3.1, 3.2, 2.9, 2.7, 2.9, 2.6])

    # ave speed in each direction (m/s)
    ave_speeds = np.array([6.3, 6.9, 6.9, 5.9, 5.7, 5.4, 4.3, 4.4, 4.9, 5.3, 5.1, 5.5, 5.3, 5.4, 4.9, 5.0, 4.8, 4.7,
                           4.5, 4.8, 4.7, 4.9, 5.2, 5.7, 6.2, 6.4, 5.9, 5.5, 5.4, 5.5, 5.7, 5.9, 5.9, 6.0, 6.0, 5.7])

    # directions corresponding to speeds above (deg)
    directions = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                           210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350])

    din = np.hstack([-np.flip(directions, 0), directions, directions[1:] + 360.])
    fin = np.hstack([-np.flip(frequencies, 0), frequencies, frequencies[1:] + 360.])
    sin = np.hstack([-np.flip(directions, 0), directions, directions[1:] + 360.])
    # print t
    # quit()
    nDirections = 20
    freq_func = interp1d(din,fin)
    speed_func = interp1d(np.hstack([-directions, directions, directions+360.]),
                                  np.hstack([ave_speeds, ave_speeds, ave_speeds]))
    freq = np.zeros(nDirections)
    aspeeds = np.zeros(nDirections)
    directions = np.linspace(0, 360, nDirections)
    width = 360./nDirections
    nSamples = 20.
    for d, i in zip(np.arange(0, nDirections), directions):
        low = int(d-width/2.)
        high = int(d+width/2.)

        freq[i] = quad(freq_func, low, high)
        aspeeds[i] = quad(speed_func, low, high)

    np.savetxt("nantucket_windrose_ave_speeds_%dirs.txt" % nDirections, np.c_[directions, aspeeds, freq],
               header="directions, average speeds, frequencies")