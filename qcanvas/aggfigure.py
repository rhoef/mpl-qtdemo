"""
aggfigure.py
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'WTFL'

__all__ = ['agg_figure']

from matplotlib.figure import Figure

def agg_figure():
    fig = Figure()
    # import pdb; pdb.set_trace()
    ax = fig.add_subplot(111)
    ax.plot([1,2,3])
    ax.set_title('hi mom')
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('volts')
    return fig
