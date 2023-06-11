import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QRadioButton)
from PyQt5.QtGui import QPixmap


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(400, 500, 400, 600)
        self.setWindowTitle("Ejercicio pajero")

        # Creo diccionario con conjunto de widgets del tipo labels

        self.labels = {}
        self.labels["label1"] = QLabel("Usuario: ", self)
        self.labels["label1"].move(50, 20)
        self.labels["label2"] = QLabel("Género: ", self)
        self.labels["label2"].move(50, 100)
        self.labels["label3"] = QLabel("Edad: ", self)
        self.labels["label3"].move(50, 160)
        self.labels["label4"] = QLabel("Configuración: ", self)
        self.labels["label4"].move(50, 220)

        # QlineEdit

        self.edit = QLineEdit("", self)
        self.edit.move(120, 20)

        # RadioButtons

        self.button1 = QRadioButton("Masculino", self)
        self.button1.move(120, 75)
        self.button2 = QRadioButton("Femenino", self)
        self.button2.move(120, 105)
        self.button3 = QRadioButton("No mencionar", self)
        self.button3.move(120, 140)
        self.show()
     

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    
    sys.exit(app.exec())