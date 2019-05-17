import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, \
                            QGroupBox, QComboBox, QPushButton, \
                            QTextEdit, QLineEdit


class GeneralUI(QWidget):
    def __init__(self):
        super().__init__()

        self.InitUI()

    def InitUI(self):
        port_cmb = QComboBox()
        baudrate_cmb = QComboBox()
        refresh_btn = QPushButton('Refresh')
        connect_btn = QPushButton('Connect')

        serial_vbox1 = QVBoxLayout()
        serial_vbox1.addWidget(port_cmb)
        serial_vbox1.addWidget(baudrate_cmb)
        serial_vbox2 = QVBoxLayout()
        serial_vbox2.addWidget(refresh_btn)
        serial_vbox2.addWidget(connect_btn)
        serial_hbox = QHBoxLayout()
        serial_hbox.addLayout(serial_vbox1)
        serial_hbox.addLayout(serial_vbox2)

        group_box = QGroupBox('Serial')
        group_box.setLayout(serial_hbox)

        receive_te = QTextEdit()
        receive_te.setDisabled(True)

        send_le = QLineEdit()
        send_btn = QPushButton('Send')

        send_hbox = QHBoxLayout()
        send_hbox.addWidget(send_le, 4)
        send_hbox.addWidget(send_btn, 1)

        vbox = QVBoxLayout()
        vbox.addWidget(group_box)
        vbox.addWidget(receive_te)
        vbox.addLayout(send_hbox)
        self.setLayout(vbox)
