# Frontend
# ventana.py
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)
from calculadora import Calculadora


class Ventana(QWidget):
    senal_calcular = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        
        
        self.label1 = QLabel("Valor 1: ", self)
        self.label1.resize(self.label1.sizeHint())

        self.label2 = QLabel("Valor 2: ", self)
        self.label2.resize(self.label2.sizeHint())
        
        self.escribir1 = QLineEdit("", self)
        self.escribir1.resize(self.escribir1.sizeHint())

        self.escribir2 = QLineEdit("", self)
        self.escribir2.resize(self.escribir2.sizeHint())

        self.boton_suma = QPushButton("+", self)
        self.boton_suma.resize(self.boton_suma.sizeHint())
        self.boton_suma.clicked.connect(self.boton_clickeado_suma)
        self.boton_rest = QPushButton("-", self)
        self.boton_rest.resize(self.boton_rest.sizeHint())
        self.boton_rest.clicked.connect(self.boton_clickeado_resta)
        self.boton_mult = QPushButton("x", self)
        self.boton_mult.resize(self.boton_mult.sizeHint())
        self.boton_mult.clicked.connect(self.boton_clickeado_mult)
        self.boton_divi = QPushButton("/", self)
        self.boton_divi.resize(self.boton_divi.sizeHint())
        self.boton_divi.clicked.connect(self.boton_clickeado_divi)
        
        self.resultado = QLabel("Resultado: ", self)
        self.resultado.resize(self.resultado.sizeHint())

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton_suma)
        hbox.addWidget(self.boton_rest)
        hbox.addWidget(self.boton_mult)
        hbox.addWidget(self.boton_divi)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.escribir1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.escribir2)
        vbox.addWidget(self.resultado)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Calculadora Back/Front End")
        self.show()

    def boton_clickeado_suma(self):
        v1 = self.escribir1.text()
        v2 = self.escribir2.text()
        diccionario = {"operacion": "sumar", "valor1": v1, "valor2": v2}
        print(f"genere diccionario {diccionario}")
        self.senal_calcular.emit(diccionario)

    def boton_clickeado_resta(self):
        v1 = self.escribir1.text()
        v2 = self.escribir2.text()
        diccionario = {"operacion": "restar", "valor1": v1, "valor2": v2}
        self.senal_calcular.emit(diccionario)

    def boton_clickeado_mult(self):
        v1 = self.escribir1.text()
        v2 = self.escribir2.text()
        diccionario = {"operacion": "multiplicar", "valor1": v1, "valor2": v2}
        self.senal_calcular.emit(diccionario)

    def boton_clickeado_divi(self):
        v1 = self.escribir1.text()
        v2 = self.escribir2.text()
        diccionario = {"operacion": "dividir", "valor1": v1, "valor2": v2}
        self.senal_calcular.emit(diccionario)

    def actualizar_front(self, texto):
        self.resultado.setText(f"Resultado: {texto}")
        self.resultado.resize(self.resultado.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    calculadora = Calculadora()
    ventana = Ventana()

    # conectar señales a continuación
    # Recuerda conectar cada señal con el método de la clase que corresponda
    ventana.senal_calcular.connect(calculadora.validar_input)
    calculadora.senal_mostrar_resultado.connect(ventana.actualizar_front)
    
    sys.exit(app.exec())

    