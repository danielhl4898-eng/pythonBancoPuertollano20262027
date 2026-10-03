from audioop import error

from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        if tipo == "movimientos":
            return leerFichero(num)

        elif tipo == "guardado":
            return cargarClienteGuardado(num)


def leerFichero(numCliente):


    log.escribir("INFO", f"INICIO CARGA DEL CLIENTE:{numCliente}")
    cliente = Cliente(numCliente)

    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:
            #contador de numero de lineas
            nunLinea = 0
            linea = f.readline()

            while linea:
                nunLinea +=1
                datos = linea.strip().split(";")
                #si la cantidad no es numerica, ignoramos la linea y registramos en el log
                try:
                    cantidad = float(datos[0])
                    operacion = datos[1]
                    destino = datos[2]

                    if destino == "Cuenta" and operacion == "Ingreso":
                        cliente.cuenta.ingresar(cantidad)

                    elif destino == "Cuenta" and operacion == "Retirada":
                        cliente.cuenta.retirar(cantidad)

                    elif destino == "Deposito" and operacion == "Ingreso":
                        cliente.deposito.ingresar(cantidad)

                    elif destino == "Deposito" and operacion == "Retirada":
                        cliente.deposito.retirar(cantidad)
                    #recogemos como excepcion que el destino o la oprecion no sean las establecidas
                    else:
                        raise NameError (f"Operación o destino incorrectos en la linea {nunLinea}")

                except ValueError:
                    log.escribir("ERROR",
                             f"La cantidad de la linea {nunLinea} no es un numero valido")
                except NameError as e:
                    log.escribir("WARNING",
                                  f"{e}")
                linea = f.readline()


        log.escribir("INFO", f"CLIENTE CARGADO CORRECTAMENTE: {numCliente}")
        # Guardamos el estado final del cliente
        cliente.guardar()

        print("Datos del cliente cargados correctamente\n")

        mostrarDatosCliente(cliente)

        return cliente

    except FileNotFoundError:
        log.escribir("ERROR",
                     f"FICHERO DE MOVIMIENTOS INEXISTENTE (cliente:{numCliente})")
        print("El usuario no tiene ninguna cuenta con el banco")
        return None




def cargarClienteGuardado(numCliente):

    try:
        with open(f"datosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()
            datos = linea.split(";")

            cliente = Cliente(datos[0])

            cliente.cuenta.saldo = float(datos[1])
            cliente.deposito.saldo = float(datos[2])

            return cliente

    except FileNotFoundError:
        log.escribir("ERROR",
                     f"INTENTO DE CONSULTA DE CLIENTE NO CARGADO:´{numCliente}")
        print("Primero tienes que cargar los datos de este cliente")
        return None

def mostrarDatosCliente(cliente):
    print(f"Cliente: {cliente.getNumero()}\n"
          f"Saldo de la cuenta: {cliente.getCuenta().getSaldo()}\n"
          f"Saldo del depósito: {cliente.getDeposito().getSaldo()}\n")