import sys
from PyQt5.QtWidgets import (QPushButton, QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Ventana evento')
        self.init_gui()

    def init_gui(self):
        self.contador = 0
        self.label = QLabel(f"{self.contador} clics")
        # self.label.move(100, 100)

        
        self.boton1 = QPushButton('Sumar 1', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.clicked.connect(self.boton_clickeado)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.boton1)
        self.setLayout(vbox)
        self.move(900, 100)

    def boton_clickeado(self):
        self.contador += 1
        self.label.setText(f'{self.contador} clics')

if __name__ == '__main__':
    app = QApplication([]) # crea interfaz gráfica
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())