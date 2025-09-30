class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto

    def consultar(self):
        return self.saldo

cuenta = CuentaBancaria("marco", 1000)
cuenta.depositar(250)
cuenta.retirar(400)
print("Saldo:", cuenta.consultar())
