import sys
from PyQt5.QtWidgets import (QPushButton, QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Ventana evento')
        self.init_gui()
    
    def init_gui(self):
        self.label1 = QLabel("Blanco")
        self.rectangulo = QPixmap().fill(Qt.white)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_k:
            self.label1.setText("uwu")

            self.rectangulo.fill(Qt.blue)


if __name__ == '__main__':
    app = QApplication([]) # crea interfaz gráfica
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())