from datetime import datetime
import os


class Log:
    tiposValidos = ("INFO", "WARNING", "ERROR")

    def __init__(self):
        fecha = datetime.now().strftime("%Y%m%d")
        self.ruta = f"log/{fecha}-banco.log"

        if not os.path.exists("log"):
            os.mkdir("log")

    def escribir(self, tipo, mensaje):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #Esto lo hago porque como solo queremos 3 tipos de errores (los de arriba)
    #en caso de que le entre un tipo que no es ninguno de esos 3, lo convierte automáticamente en info
        if tipo not in self.tiposValidos:
            tipo = "INFO"

        with open(self.ruta, "a") as fichero:
            fichero.write(f"[{fecha_hora}] [{tipo.upper()}] {mensaje}\n")
