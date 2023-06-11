import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
    
    def init_gui(self):

        self.setGeometry(200, 400, 600, 600)
        self.setWindowTitle("primeraa ventana")

        self.show()

# QLabel.Setstylesheet({"Font-size"}: float? int? px)

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    
    sys.exit(app.exec())