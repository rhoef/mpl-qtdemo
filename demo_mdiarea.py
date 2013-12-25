"""
demo_mdiarea.py
"""

__author__ = 'rudolf.hoefler@gmail.com'
__copyright__ = 'LGPL'


import sys
from PyQt4 import QtGui
from qcanvas import QFigureWidget, agg_figure

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(800 , 600)
        self._mdi = QtGui.QMdiArea(self)
        self.setCentralWidget(self._mdi)

    def cascade(self):
        self._mdi.cascadeSubWindows()

    def add_figure(self, title, fig):
        fw = QFigureWidget(fig, self)
        self._mdi.addSubWindow(fw)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    for i in xrange(3):
        fig = agg_figure()
        mw.add_figure("tab no. %d" %i, fig)
    mw.cascade()

    mw.show()
    app.exec_()

