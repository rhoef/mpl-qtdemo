"""
aggfigure.py
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'LGPL'

__all__ = ['agg_figure']

from matplotlib.figure import Figure

def agg_figure():
    """Matplotlib figure using the Agg-backend, no Qt4 or whatever"""
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot([1,2,3])
    ax.set_title('foobar')
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('volts')
    return fig
