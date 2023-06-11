import sys
from threading import Thread
from time import sleep
from random import randint
from PyQt5.QtCore import pyqtSignal, QThread, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
from os.path import join

class MiThread(QThread):
    """
    Esta clase representa un thread personalizado que será utilizado durante
    la ejecución de la GUI.
    """

    def __init__(self, senal_actualizar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.senal_actualizar = senal_actualizar

    def run(self):
        for i in range(10):
            i = randint(-8, 8)
            i2 = randint(-8, 8)
            sleep(0.5)
            self.senal_actualizar.emit(i*10, i2*10)

        sleep(0.5)
        



class MiVentana(QWidget):

    # Creamos una señal para manejar la respuesta del thread
    senal_thread = pyqtSignal(int, int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.thread = None
        # Conectamos la señal del thread al método que maneja
        self.senal_thread.connect(self.actualizar_posicion)
        self.random1 = randint(10, 450)
        self.random2 = randint(10, 450)
        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Botón verde que corre")

        self.labelImagen = QLabel(self)
        self.labelImagen.setGeometry(200, 200, 50, 50)
        ruta = join("img", "verde.png")
        self.pixeles = QPixmap(ruta)
        self.labelImagen.setPixmap(self.pixeles)
        self.labelImagen.setScaledContents(True)

        self.show()
        self.labelImagen.show()
        

    def ejecutar_threads(self):
        """
        Este método crea un thread cada vez que se presiona el botón en la
        interfaz. El thread recibirá como argumento la señal sobre la cual
        debe operar.
        """
        if self.thread is None or not self.thread.isRunning():
            self.thread = MiThread(self.senal_thread)
            self.thread.senal_actualizar.connect(self.actualizar_posicion)
            self.thread.start()

    def actualizar_posicion(self, int1, int2):
        
        self.labelImagen.move(randint(-100, 100), randint(-100, 100))

    
    def mousePressEvent(self, event):
        pos = self.labelImagen.getContentsMargins()

        if event.y() < 250:
            self.ejecutar_threads()

if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec())