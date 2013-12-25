"""
demo_tabwidget.py

Layouting matplotlib figure using a QTabWidget.

Note:
The Figure uses the Agg-backend --> figure can be emitted as PyQt_PyObject
from within a thread.
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'LGPL'


import sys
import sip
sip.setapi('QString', 2)

from PyQt4 import QtGui
from PyQt4 import QtCore
from qcanvas import *


class FigureThread(QtCore.QThread):

    figureReady = QtCore.pyqtSignal(str, "PyQt_PyObject")

    def run(self):
        for i in xrange(10):
            fig = agg_figure()
            self.figureReady.emit("tab no. %d" %i, fig)
            self.msleep(100)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    mw = QFigureTabWidget()
    mw.resize(800,600)
    fthread = FigureThread()
    fthread.figureReady.connect(mw.add_figure)
    mw.show()

    fthread.start()
    app.exec_()

