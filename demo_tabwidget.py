"""
demo_tabwidget.py

Layouting matplotlib figure using a QTabWidget.

Note:
The Figure uses the Agg-backend --> figure can be emitted as PyQt_PyObject
from within a thread.
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'WTFL'


import sys
from PyQt4 import QtGui
from qcanvas import *


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw = QFigureTabWidget()
    for i in xrange(3):
        fig = agg_figure()
        mw.add_figure("tab no. %d" %i, fig)

    mw.show()
    app.exec_()

