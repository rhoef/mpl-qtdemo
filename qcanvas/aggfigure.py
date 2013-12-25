"""
aggfigure.py
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'LGPL'

__all__ = ['agg_figure']

import time
import numpy as np
from matplotlib.figure import Figure


def agg_figure():
    """Matplotlib figure using the Agg-backend, no Qt4 or whatever"""
    fig = Figure()
    ax = fig.add_subplot(111)

    current_time = time.time()
    x = np.linspace(0, 1, 100)
    y = np.sin(10*(x+np.radians(current_time)))

    ax.plot(x, y)
    ax.set_title(time.ctime())
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('volts')
    return fig
