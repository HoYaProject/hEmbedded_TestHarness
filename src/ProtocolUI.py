import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, \
                            QLabel, QPushButton


class ProtocolUI(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.btn = QPushButton('File Open')

        self.InitUI()

    def InitUI(self):
        self.btn.clicked.connect(self.openFile)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label, 3)
        hbox.addWidget(self.btn, 1)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'File Open', './config/protocol')
        self.label.setText(fname[0])
        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
