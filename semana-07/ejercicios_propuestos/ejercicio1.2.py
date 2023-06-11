import sys
from threading import Thread
from time import sleep
from random import randint
from PyQt5.QtCore import pyqtSignal, QThread, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
from os.path import join

class Rectangulo(QThread): # es buena idea dejarlo como Qthread o es mejor usarlo como QWidget?
    
    actualizar = pyqtSignal(QLabel, int, int)
    
    def __init__(self, parent, multiplicador):
        
        self.multiplicador = multiplicador
        self.limite_mayor = 75
        self.limite_menor = 25
        """
        Una Comida es un QThread que movera una imagen de comida
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            limite_x e limite_y: Los límites rectangulares de la ventana
        """
        super().__init__()

        # Guardamos el path de la imagen que tendrá el Label
        self.ruta_imagen = join("img", "verde.png")
        
        # Creamos el Label y definimos su tamaño
        self.label = QLabel(parent)
        self.label.setGeometry(100, 50, 50, 50)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)

        # Seteamos la posición inicial y la guardamos para usarla como una property
        self.__tamano = (0, 0)
        self.tamano = (25, 25)

        self.label.show()
        self.start()

    @property
    def tamano(self):
        return self.__tamano

    # Cada vez que se actualicé la posición,
    # se actualiza la posición de la etiqueta
    @tamano.setter
    def tamano(self, valor):
        self.__tamano = valor
        self.label.resize(*self.tamano)

    def run(self):
        while self.tamano[0] < self.limite_mayor \
            and self.tamano[0] < self.limite_menor:
            sleep(0.1)
            
            # si topa bordes cambia el sentido de actualizacion de tamano
            if self.tamano[0] == self.limite_mayor or self.tamano[0] == self.limite_menor:
                self.multiplicador *= -1
            
            nuevo_x = self.tamano[0] + (1*self.multiplicador)
            nuevo_y = self.tamano[1] + (1*self.multiplicador)
            self.tamano = (nuevo_x, nuevo_y)

class MiVentana(QWidget):

    # Creamos una señal para manejar la respuesta del thread
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.timer_crea_comida = QTimer(self)
        self.timer_crea_comida.setInterval(50)
        self.timer_crea_comida.timeout.connect(self.crear_rectangulos)
        self.timer_crea_comida.start()
        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Botón verde que corre")

        # botones

        self.button_start = QPushButton("Iniciar", self)
        self.button_start.resize(self.button_start.sizeHint())
        self.button_start.clicked.connect()

        self.button_end = QPushButton("Finalizar", self)
        self.button_end.resize(self.button_end.sizeHint())
        self.button_end.clicked.connect()

        self.show()
        self.labelImagen1.show()

    def actualizar_tamano(self, int1, int2):
        
        self.labelImagen1.move(randint(-100, 100), randint(-100, 100))

    def ejecutar_threads(self):
        """
        Este método crea un thread cada vez que se presiona el botón en la
        interfaz. El thread recibirá como argumento la señal sobre la cual
        debe operar.
        """
        # Aquí debemos ocupar isRunning en lugar de is_alive
        for i in range(2):
            if self.thread is None or not self.thread.isRunning():
                self.thread = Rectangulo()
                self.thread.start()

    


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana() 
    sys.exit(app.exec())