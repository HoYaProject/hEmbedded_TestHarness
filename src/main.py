import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QTabWidget
import GeneralUI as gui
import ProtocolUI as pui
import ScriptUI as sui

class hETH(QMainWindow):
    def __init__(self):
        super().__init__()

        self.InitUI()

    def InitUI(self):
        tabs = QTabWidget(self)
        tabs.addTab(gui.GeneralUI(), 'General')
        tabs.addTab(pui.ProtocolUI(), 'Protocol')
        tabs.addTab(sui.ScriptUI(), 'Script')

        self.setCentralWidget(tabs)
        self.setWindowTitle('hEmbedded_TestHarness')
        self.setGeometry(300, 300, 500, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = hETH()
    sys.exit(app.exec_())
