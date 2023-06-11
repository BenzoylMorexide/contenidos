import threading
import time


class CuentaOvejas(threading.Thread): # Hereda de Thread
    """Este será nuestro nuevo Cuenta Ovejas basado en Thread"""
    
    def __init__(self, nombre, max_ovejas):
        # En el caso de los threads, lo primero es invocar al init original. SIEMPRE.
        super().__init__(name=nombre)
        self.max_ovejas = max_ovejas # Se agrega un atributo de instancia extra
    
    def run(self):
        # Este metodo define las instrucciones a ejecutar de este thread
        # cuando ejecutamos el metodo start()
        print(f"{self.name} tiene sueño...")
        tiempo_partida = time.time()
        for numero in range(1, self.max_ovejas + 1):
            time.sleep(1)
            print(f"({self.name}: {numero} oveja{'s' if numero > 1 else ''})")
        print(f"{self.name} a dormir...")
        print(f"{self.name} se durmió después de {time.time() - tiempo_partida} seg.")

        
class CuentaLiebres(threading.Thread): # Hereda de Thread
    """
    Este será un nuevo Cuenta Liebres basado en Thread
    Las liebres son más rápidas, así que cuenta dos por segundo
    """
    
    def __init__(self, nombre, max_liebres):
        super().__init__(name=nombre)
        self.max_liebres = max_liebres
    
    def run(self):
        print(f"{self.name} tiene sueño...")
        tiempo_partida = time.time()
        for numero in range(1, self.max_liebres + 1):
            if numero % 2 == 1:
                time.sleep(1)
            print(f"({self.name}: {numero} liebre{'s' if numero > 1 else ''})")
        print(f"{self.name} a dormir...")
        print(f"{self.name} se durmió después de {time.time() - tiempo_partida} seg.")
        

# Se crean los threads
hernan = CuentaOvejas("Hernán", 5)
daniela = CuentaOvejas("Daniela", 7)
dante = CuentaLiebres("Dante", 5)
joaquin = CuentaLiebres("Joaquín", 10)

# Se inicializan los threads creados
hernan.start()
daniela.start()
dante.start()
joaquin.start()
daniela.join()  # Esperaremos lo que sea necesario.
print("Ayudantes: ¡DANIELA SE DURMIÓ!")
hernan.join() # No especificamos timeout, esperará lo que sea necesario
print("Ayudantes: ¡HERNÁN SE DURMIÓ!")
dante.join() # Esperaremos lo que sea necesario.
print("Ayudantes: ¡DANTE SE DURMIÓ!")
joaquin.join(1)  # Esperaremos máximo 1 segundos después del último dormido, ya es muy tarde

if joaquin.is_alive():
    print("Ayudantes: Joaquín sigue despierto 😞. A la casa cabros.")
else:
    print("Ayudantes: ¡Todos los profes se durmieron! ¡A festejar!")
    for i in range(6):
        print("Ayudantes: 🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶")
        time.sleep(1)