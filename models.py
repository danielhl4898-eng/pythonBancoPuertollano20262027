import os

class CuentaBancaria:

    def __init__(self):
        self.saldo = 0

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def getSaldo(self):
        return self.saldo


class Deposito:

    def __init__(self):
        self.saldo = 0

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def getSaldo(self):
        return self.saldo


class Cliente:

    def __init__(self, numero):
        self.numero = numero
        self.cuenta = CuentaBancaria()
        self.deposito = Deposito()

    def getNumero(self):
        return self.numero

    def getCuenta(self):
        return self.cuenta

    def getDeposito(self):
        return self.deposito

    def guardar(self):
        if not os.path.exists("datosClientes"):
            os.mkdir("datosClientes")

        with open(f"datosClientes/{self.numero}.txt", "w") as f:
            #Cambio los ";" por saltos de línea
            f.write(
                f"{self.numero}\n"
                f"{self.cuenta.getSaldo()}\n"
                f"{self.deposito.getSaldo()}"
            )


    def getSaldoTotal(self):
        total = self.cuenta.getSaldo() + self.deposito.getSaldo()
        return total