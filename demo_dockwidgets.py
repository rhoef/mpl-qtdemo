"""
demo_dockwidgets.py

Example uses QDockWidgets (i.e. a QMainWindow). The figures are tabified by
default but can be floating or moved to a different dockwidgetarea.

Note:
The Figure uses the Agg-backend --> figure can be emitted as PyQt_PyObject
from within a thread.
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'WTFL'


import sys
from collections import OrderedDict
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from qcanvas import *


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self._dockwidgets = OrderedDict()

    def tabifyDockWidgets(self):
        dw0 = self._dockwidgets.values()[0]
        for dw in self._dockwidgets.itervalues():
            if dw is not dw0:
                self.tabifyDockWidget(dw0, dw)

    def add_figure(self, title, fig):
        dw = QtGui.QDockWidget(title, self)
        fw = QFigureWidget(fig, dw)

        dw.setWidget(fw)
        self._dockwidgets[title] = dw
        self.addDockWidget(Qt.LeftDockWidgetArea, dw)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    for i in xrange(3):
        fig = agg_figure()
        mw.add_figure("tab no. %d" %i, fig)

    mw.tabifyDockWidgets()
    mw.show()
    app.exec_()

